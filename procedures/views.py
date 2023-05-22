from django.shortcuts import render, reverse
from .models import Procedure
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import ProcedureForm
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class ProcedureListView(LoginRequiredMixin, ListView):
    model = Procedure
    template_name = "procedures/procedures.html"
    context_object_name = "procedures"
    ordering = ["name"]


class ProcedureCreateView(LoginRequiredMixin, CreateView):
    model = Procedure
    form_class = ProcedureForm
    template_name = "procedures/procedure_form.html"

    def get_success_url(self):
        return reverse("procedures:procedures")


class ProcedureUpdateView(LoginRequiredMixin, UpdateView):
    model = Procedure
    form_class = ProcedureForm
    template_name = "procedures/procedure_update_form.html"

    def get_success_url(self):
        return reverse("procedures:procedures")


class ProcedureDeleteView(LoginRequiredMixin, DeleteView):
    model = Procedure

    def get_success_url(self):
        return reverse("procedures:procedures")
