import os
from django.conf import settings
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from io import BytesIO
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from django.views.generic import ListView

from records.models import Visit
from .models import Invoice


def generate_invoice(visit_id):
    visit = get_object_or_404(Visit, pk=visit_id)
    owner = visit.animal_case.animal.owner
    year = visit.created_at.strftime("%Y")

    font_path = os.path.join(settings.BASE_DIR, "static", "fonts", "DejaVuSans.ttf")
    pdfmetrics.registerFont(TTFont("DejaVuSans", font_path))
    font_path_bold = os.path.join(
        settings.BASE_DIR, "static", "fonts", "DejaVuSans-Bold.ttf"
    )
    pdfmetrics.registerFont(TTFont("DejaVuSans-Bold", font_path_bold))
    # Zde můžete nastavit vlastnosti PDF, jako je název, fonty atd.
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)
    pdf.setTitle("Faktura návštěvy")
    pdf.setFont("DejaVuSans", 12)

    # Nadpis Faktura
    pdf.setFont("DejaVuSans-Bold", 20)
    pdf.drawString(10 * mm, 270 * mm, "Faktura")

    # Číslo faktury
    invoice_number = f"{year}{visit.pk}"
    pdf.setFont("DejaVuSans", 12)
    pdf.drawString(140 * mm, 270 * mm, f"Číslo faktury: {invoice_number}")

    # Dodavatel
    pdf.setFont("DejaVuSans-Bold", 12)
    pdf.drawString(10 * mm, 250 * mm, "DODAVATEL:")
    pdf.drawString(10 * mm, 245 * mm, "Veteriární klinika")
    pdf.setFont("DejaVuSans", 12)
    pdf.drawString(10 * mm, 240 * mm, "Ulice 123")
    pdf.drawString(10 * mm, 235 * mm, "123 45 Město")
    pdf.drawString(10 * mm, 230 * mm, "Česká republika")

    # Variabilní symbol a forma úhrady
    pdf.drawString(10 * mm, 220 * mm, f"Variabilní symbol: {invoice_number}")
    pdf.drawString(10 * mm, 215 * mm, "Forma úhrady: Hotově")

    # Majitel
    pdf.setFont("DejaVuSans-Bold", 12)
    pdf.drawString(110 * mm, 250 * mm, "MAJITEL:")
    pdf.drawString(110 * mm, 245 * mm, f"{owner.first_name} {owner.last_name}")
    pdf.setFont("DejaVuSans", 12)
    pdf.drawString(110 * mm, 240 * mm, f"{owner.street} {owner.house_number}")
    pdf.drawString(110 * mm, 235 * mm, f"{owner.postal_code} {owner.city}")
    pdf.drawString(110 * mm, 230 * mm, f"{owner.country}")

    invoice_date = visit.updated_at.strftime("%d.%m.%Y")
    # Datum vystavení a splatnosti
    pdf.drawString(110 * mm, 220 * mm, f"Datum vystavení: {invoice_date}")
    pdf.drawString(110 * mm, 215 * mm, f"Datum splatnosti: {invoice_date}")

    # Zvíře
    pdf.setFont("DejaVuSans-Bold", 12)
    pdf.drawString(10 * mm, 200 * mm, f"Zvíře: {visit.animal_case.animal.name}")

    # Nadpisy pro položky
    pdf.setFont("DejaVuSans", 12)
    pdf.drawString(10 * mm, 190 * mm, "Název položky")
    pdf.drawRightString(130 * mm, 190 * mm, "MJ")
    pdf.drawRightString(160 * mm, 190 * mm, "Cena za MJ")
    pdf.drawRightString(190 * mm, 190 * mm, "Cena")

    # Oddělující čára
    pdf.setLineWidth(1)
    pdf.line(10 * mm, 185 * mm, 190 * mm, 185 * mm)

    # Seznam položek
    pdf.setFont("DejaVuSans", 10)
    y = 180 * mm
    for item in visit.stock_items.all():
        pdf.drawString(10 * mm, y, f"{item.stock_item.name}")
        pdf.drawRightString(130 * mm, y, f"{item.quantity}")
        pdf.drawRightString(160 * mm, y, f"{item.stock_item.selling_price} Kč")
        pdf.drawRightString(190 * mm, y, f"{item.price} Kč")
        y -= 5 * mm

    for procedure in visit.procedures.all():
        pdf.drawString(10 * mm, y, f"{procedure.procedure.name}")
        pdf.drawRightString(130 * mm, y, "-")
        pdf.drawRightString(160 * mm, y, "-")
        pdf.drawRightString(190 * mm, y, f"{procedure.price} Kč")
        y -= 5 * mm

    pdf.setLineWidth(3)
    pdf.line(10 * mm, y - 5 * mm, 190 * mm, y - 5 * mm)

    # Celková cena
    pdf.setFont("DejaVuSans", 16)
    pdf.drawString(10 * mm, y - 15 * mm, f"Celková cena: {visit.price} Kč")

    pdf.showPage()
    pdf.save()

    buffer.seek(0)
    return buffer


class InvoiceListView(ListView):
    model = Invoice
    template_name = "accounting/invoice_list.html"
    context_object_name = "invoices"

    def get_queryset(self):
        return Invoice.objects.order_by("-generated_at")


def invoice_pdf_view(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    buffer = BytesIO(invoice.content)
    response = FileResponse(buffer, content_type="application/pdf")
    response[
        "Content-Disposition"
    ] = f"inline; filename=faktura-{invoice.generated_at.year}{invoice.visit.pk:06}.pdf"
    return response
