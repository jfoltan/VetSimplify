from django.urls import path
from .views import generate_invoice

app_name = "accounting"

urlpatterns = [
    path(
        "generate_invoice/<int:visit_id>/",
        generate_invoice,
        name="generate_invoice",
    ),
]
