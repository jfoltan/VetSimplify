from django.shortcuts import render, reverse
from .models import Procedure
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import ProcedureForm


# Create your views here.
class ProcedureListView(ListView):
    model = Procedure
    template_name = "procedures/procedures.html"
    context_object_name = "procedures"
    ordering = ["name"]


class ProcedureCreateView(CreateView):
    model = Procedure
    form_class = ProcedureForm
    template_name = "procedures/procedure_form.html"

    def get_success_url(self):
        return reverse("procedures:procedures")


class ProcedureUpdateView(UpdateView):
    model = Procedure
    form_class = ProcedureForm
    template_name = "procedures/procedure_update_form.html"

    def get_success_url(self):
        return reverse("procedures:procedures")


class ProcedureDeleteView(DeleteView):
    model = Procedure

    def get_success_url(self):
        return reverse("procedures:procedures")
