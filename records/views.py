from typing import Any, Dict
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
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

# Create your views here.


class OwnerListView(ListView):
    model = Owner


class OwnerDetailView(DetailView):
    model = Owner

    def get_object(self):
        owner_id = self.kwargs["owner_id"]
        return get_object_or_404(Owner, pk=owner_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["animal_list"] = Animal.objects.filter(owner=self.object)
        return context


class OwnerCreateView(CreateView):
    model = Owner
    form_class = OwnerForm
    template_name = "records/owner_form.html"

    def get_success_url(self):
        return reverse_lazy("records:owner_detail", kwargs={"owner_id": self.object.pk})


class OwnerUpdateView(UpdateView):
    model = Owner
    form_class = OwnerForm
    template_name = "records/owner_update_form.html"

    def get_object(self):
        owner_id = self.kwargs["owner_id"]
        return get_object_or_404(Owner, pk=owner_id)

    def get_success_url(self):
        return reverse_lazy("records:owner_detail", kwargs={"owner_id": self.object.pk})


class OwnerDeleteView(DeleteView):
    model = Owner
    success_url = reverse_lazy("records:owner_list")


class AnimalCreateView(CreateView):
    model = Animal
    form_class = AnimalForm
    template_name = "records/animal_form.html"

    def form_valid(self, form):
        owner_id = self.kwargs["owner_id"]
        owner = get_object_or_404(Owner, pk=owner_id)
        form.instance.owner = owner
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["owner"] = get_object_or_404(Owner, pk=self.kwargs["owner_id"])
        return context

    def get_success_url(self):
        return reverse_lazy(
            "records:owner_detail", kwargs={"owner_id": self.kwargs["owner_id"]}
        )


class AnimalDetailView(DetailView):
    model = Animal

    def get_object(self):
        owner_id = self.kwargs["owner_id"]
        animal_id = self.kwargs["animal_id"]
        return get_object_or_404(Animal, owner_id=owner_id, pk=animal_id)


class AnimalUpdateView(UpdateView):
    model = Animal
    form_class = AnimalForm
    template_name = "records/animal_update_form.html"

    def get_object(self):
        owner_id = self.kwargs["owner_id"]
        animal_id = self.kwargs["animal_id"]
        return get_object_or_404(Animal, owner_id=owner_id, pk=animal_id)

    def get_success_url(self):
        return reverse_lazy(
            "records:owner_detail", kwargs={"owner_id": self.kwargs["owner_id"]}
        )


class AnimalDeleteView(DeleteView):
    model = Animal

    def get_object(self):
        owner_id = self.kwargs["owner_id"]
        animal_id = self.kwargs["animal_id"]
        return get_object_or_404(Animal, owner_id=owner_id, pk=animal_id)

    def get_success_url(self):
        return reverse_lazy(
            "records:owner_detail", kwargs={"owner_id": self.kwargs["owner_id"]}
        )
