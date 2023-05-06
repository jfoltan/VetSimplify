from django.urls import path
from .views import generate_invoice, InvoiceListView, invoice_pdf_view

app_name = "accounting"

urlpatterns = [
    path(
        "generate_invoice/<int:visit_id>/",
        generate_invoice,
        name="generate_invoice",
    ),
    path("", InvoiceListView.as_view(), name="invoice_list"),
    path("invoices/<int:pk>/pdf/", invoice_pdf_view, name="invoice_pdf"),
]
