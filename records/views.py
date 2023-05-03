from django.shortcuts import redirect, render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from stock.models import StockItem
from .forms import OwnerForm, AnimalForm, AnimalCaseForm, VisitForm, VisitFormSet
from .models import Owner, Animal, AnimalCase, Visit
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.core import serializers


class OwnerMixin:
    def get_owner(self):
        owner_id = self.kwargs["owner_id"]
        return get_object_or_404(Owner, pk=owner_id)


class AnimalMixin(OwnerMixin):
    def get_animal(self):
        owner = self.get_owner()
        animal_id = self.kwargs["animal_id"]
        return get_object_or_404(Animal, owner=owner, pk=animal_id)


class AnimalCaseMixin(AnimalMixin):
    def get_animalcase(self):
        animal = self.get_animal()
        animalcase_id = self.kwargs["animalcase_id"]
        return get_object_or_404(AnimalCase, animal=animal, pk=animalcase_id)


class VisitMixin(AnimalCaseMixin):
    def get_visit(self):
        animal_case = self.get_animalcase()
        visit_id = self.kwargs["visit_id"]
        return get_object_or_404(Visit, animal_case=animal_case, pk=visit_id)


def get_animalcase(owner_id, animal_id, animalcase_id):
    return AnimalCase.objects.get(
        animal__owner__id=owner_id, animal__id=animal_id, id=animalcase_id
    )


class OwnerListView(ListView):
    model = Owner


class OwnerDetailView(OwnerMixin, DetailView):
    model = Owner

    def get_object(self):
        return self.get_owner()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["animal_list"] = Animal.objects.filter(owner=self.object)
        return context


class OwnerCreateView(CreateView):
    model = Owner
    form_class = OwnerForm
    template_name = "records/owner_form.html"

    def get_success_url(self):
        return reverse("records:owner_detail", kwargs={"owner_id": self.object.pk})


class OwnerUpdateView(OwnerMixin, UpdateView):
    model = Owner
    form_class = OwnerForm
    template_name = "records/owner_update_form.html"

    def get_object(self):
        return self.get_owner()

    def get_success_url(self):
        return reverse("records:owner_detail", kwargs={"owner_id": self.object.pk})


class OwnerDeleteView(OwnerMixin, DeleteView):
    model = Owner

    def get_object(self):
        return self.get_owner()

    def get_success_url(self):
        return reverse("records:owner_list")


class AnimalCreateView(OwnerMixin, CreateView):
    model = Animal
    form_class = AnimalForm
    template_name = "records/animal_form.html"

    def form_valid(self, form):
        owner = self.get_owner()
        form.instance.owner = owner
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["owner"] = self.get_owner()
        return context

    def get_success_url(self):
        return reverse(
            "records:owner_detail", kwargs={"owner_id": self.kwargs["owner_id"]}
        )


class AnimalDetailView(AnimalMixin, DetailView):
    model = Animal

    def get_object(self):
        return self.get_animal()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["animalcase_list"] = AnimalCase.objects.filter(animal=self.object)
        context["owner"] = self.get_owner()
        return context


class AnimalUpdateView(AnimalMixin, UpdateView):
    model = Animal
    form_class = AnimalForm
    template_name = "records/animal_update_form.html"

    def get_object(self):
        return self.get_animal()

    def get_success_url(self):
        return reverse(
            "records:owner_detail", kwargs={"owner_id": self.kwargs["owner_id"]}
        )


class AnimalDeleteView(AnimalMixin, DeleteView):
    model = Animal

    def get_object(self):
        return self.get_animal()

    def get_success_url(self):
        return reverse(
            "records:owner_detail", kwargs={"owner_id": self.kwargs["owner_id"]}
        )


class AnimalCaseCreateView(AnimalMixin, CreateView):
    model = AnimalCase
    form_class = AnimalCaseForm
    template_name = "records/animalcase_form.html"

    def form_valid(self, form):
        animal = self.get_animal()
        form.instance.animal = animal
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["animal"] = self.get_animal()
        return context

    def get_success_url(self):
        return reverse(
            "records:animal_detail",
            kwargs={
                "owner_id": self.kwargs["owner_id"],
                "animal_id": self.kwargs["animal_id"],
            },
        )


class AnimalCaseDetailView(AnimalCaseMixin, DetailView):
    model = AnimalCase

    def get_object(self):
        return self.get_animalcase()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["visit_list"] = Visit.objects.filter(animal_case=self.object)
        context["animal"] = self.get_animal()
        context["owner"] = self.get_owner()
        return context


class AnimalCaseUpdateView(AnimalCaseMixin, UpdateView):
    model = AnimalCase
    form_class = AnimalCaseForm
    template_name = "records/animalcase_update_form.html"

    def get_object(self):
        return self.get_animalcase()

    def get_success_url(self):
        return reverse(
            "records:animal_detail",
            kwargs={
                "owner_id": self.kwargs["owner_id"],
                "animal_id": self.kwargs["animal_id"],
            },
        )


class AnimalCaseDeleteView(AnimalCaseMixin, DeleteView):
    model = AnimalCase

    def get_object(self):
        return self.get_animalcase()

    def get_success_url(self):
        return reverse(
            "records:animal_detail",
            kwargs={
                "owner_id": self.kwargs["owner_id"],
                "animal_id": self.kwargs["animal_id"],
            },
        )


def visit_create_view(request, owner_id, animal_id, animalcase_id):
    animal_case = get_animalcase(owner_id, animal_id, animalcase_id)
    stock_items = StockItem.objects.all()
    stock_items_json = serializers.serialize(
        "json", stock_items, fields=("pk", "selling_price")
    )

    if request.method == "POST":
        visit_form = VisitForm(request.POST, prefix="visit")
        formset = VisitFormSet(request.POST, prefix="visit_stock_item")

        if visit_form.is_valid() and formset.is_valid():
            visit = visit_form.save(commit=False)
            visit.animal_case = animal_case
            visit.save()

            formset.instance = visit
            formset.save()

            for form in formset.forms:
                stock_item = form.cleaned_data.get("stock_item")
                quantity = form.cleaned_data.get("quantity")

                stock_item.units_in_stock -= quantity
                stock_item.save()

            return redirect(
                "records:animal_case_detail",
                owner_id=owner_id,
                animal_id=animal_id,
                animalcase_id=animalcase_id,
            )
    else:
        visit_form = VisitForm(prefix="visit")
        formset = VisitFormSet(instance=Visit(), prefix="visit_stock_item")

    context = {
        "visit_form": visit_form,
        "formset": formset,
        "animal_case": animal_case,
        "stock_items_json": stock_items_json,
    }
    return render(request, "records/visit_form.html", context)


def visit_delete_view(request, owner_id, animal_id, animalcase_id, visit_id):
    animal_case = get_animalcase(owner_id, animal_id, animalcase_id)
    visit = get_object_or_404(Visit, pk=visit_id, animal_case=animal_case)

    if request.method == "POST":
        # Return stock items to the stock
        for visit_stock_item in visit.stock_items.all():
            stock_item = visit_stock_item.stock_item
            stock_item.units_in_stock += visit_stock_item.quantity
            stock_item.save()

        # Delete the visit
        visit.delete()

        return redirect(
            "records:animal_case_detail",
            owner_id=owner_id,
            animal_id=animal_id,
            animalcase_id=animalcase_id,
        )

    context = {
        "visit": visit,
        "animal_case": animal_case,
    }
    return render(request, "records/visit_confirm_delete.html", context)
