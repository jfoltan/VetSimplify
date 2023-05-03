from django.urls import path
from .views import (
    ProcedureListView,
    ProcedureCreateView,
    ProcedureUpdateView,
    ProcedureDeleteView,
)

app_name = "procedures"

urlpatterns = [
    path("", ProcedureListView.as_view(), name="procedures"),
    path("create", ProcedureCreateView.as_view(), name="procedure_create"),
    path("update/<int:pk>", ProcedureUpdateView.as_view(), name="procedure_update"),
    path("delete/<int:pk>", ProcedureDeleteView.as_view(), name="procedure_delete"),
]
