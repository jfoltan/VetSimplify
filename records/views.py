from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .forms import OwnerForm
from .models import Owner
from django.urls import reverse_lazy

# Create your views here.


class OwnerListView(ListView):
    model = Owner


class OwnerDetailView(DetailView):
    model = Owner


class OwnerCreateView(CreateView):
    model = Owner
    form_class = OwnerForm
    success_url = reverse_lazy("records:owner_list")
    template_name = "records/owner_form.html"


class OwnerUpdateView(UpdateView):
    model = Owner
    form_class = OwnerForm
    template_name = "records/owner_update_form.html"

    def get_success_url(self):
        return reverse_lazy("records:owner_detail", kwargs={"pk": self.object.pk})


class OwnerDeleteView(DeleteView):
    model = Owner
    success_url = reverse_lazy("records:owner_list")
