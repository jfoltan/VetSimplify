from django.urls import path
from . import views

app_name = "accounting"

urlpatterns = [
    path(
        "generate_invoice/<int:visit_id>/",
        views.generate_invoice,
        name="generate_invoice",
    ),
]
