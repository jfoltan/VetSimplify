from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .forms import OwnerForm, AnimalForm, AnimalCaseForm, VisitForm
from .models import Owner, Animal, AnimalCase, Visit
from django.urls import reverse
from django.shortcuts import get_object_or_404


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


class VisitCreateView(AnimalCaseMixin, CreateView):
    model = Visit
    form_class = VisitForm
    template_name = "records/visit_form.html"

    def form_valid(self, form):
        animal_case = self.get_animalcase()
        form.instance.animal_case = animal_case
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["animal_case"] = self.get_animalcase()
        return context

    def get_success_url(self):
        return reverse(
            "records:animal_case_detail",
            kwargs={
                "owner_id": self.kwargs["owner_id"],
                "animal_id": self.kwargs["animal_id"],
                "animalcase_id": self.kwargs["animalcase_id"],
            },
        )


class VisitUpdateView(VisitMixin, UpdateView):
    model = Visit
    form_class = VisitForm
    template_name = "records/visit_update_form.html"

    def get_object(self):
        return self.get_visit()

    def get_success_url(self):
        return reverse(
            "records:animal_case_detail",
            kwargs={
                "owner_id": self.kwargs["owner_id"],
                "animal_id": self.kwargs["animal_id"],
                "animalcase_id": self.kwargs["animalcase_id"],
            },
        )


class VisitDeleteView(VisitMixin, DeleteView):
    model = Visit

    def get_object(self):
        return self.get_visit()

    def get_success_url(self):
        return reverse(
            "records:animal_case_detail",
            kwargs={
                "owner_id": self.kwargs["owner_id"],
                "animal_id": self.kwargs["animal_id"],
                "animalcase_id": self.kwargs["animalcase_id"],
            },
        )
