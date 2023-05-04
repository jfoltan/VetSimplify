from django.http import FileResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from io import BytesIO

from records.models import Visit


def generate_invoice(request, visit_id):
    visit = get_object_or_404(Visit, pk=visit_id)

    # Zde můžete nastavit vlastnosti PDF, jako je název, fonty atd.
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)
    pdf.setTitle("Faktura návštěvy")

    # Zde můžete přidat obsah faktury, jako je seznam položek a úkonů
    y = 800
    for item in visit.stock_items.all():
        pdf.drawString(
            50, y, f"{item.stock_item.name} ({item.quantity}) - {item.price} Kč"
        )
        y -= 20

    for procedure in visit.procedures.all():
        pdf.drawString(50, y, f"{procedure.procedure.name} - {procedure.price} Kč")
        y -= 20

    pdf.drawString(50, y, f"Celková cena: {visit.price} Kč")

    pdf.showPage()
    pdf.save()

    buffer.seek(0)
    if "generate_pdf" in request.GET:
        return FileResponse(buffer, as_attachment=True, filename="faktura.pdf")
    else:
        return HttpResponseRedirect(
            reverse(
                "records:animal_case_detail",
                args=[
                    visit.animal_case.owner.pk,
                    visit.animal_case.animal.pk,
                    visit.animal_case.pk,
                ],
            )
        )
