from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .forms import OwnerForm, AnimalForm
from .models import Owner, Animal
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
