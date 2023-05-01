from django import forms
from .models import StockItem
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div


class StockItemForm(forms.ModelForm):
    class Meta:
        model = StockItem
        fields = [
            "stock",
            "name",
            "type",
            "supplier_code",
            "supplier",
            "expiration_date",
            "ean",
            "batch",
            "units_in_stock",
            "units_in_package",
            "purchase_price",
            "selling_price",
            "margin",
            "note",
        ]
        labels = {
            "stock": "Sklad",
            "name": "Název",
            "type": "Typ položky",
            "supplier_code": "Kód dodavatele",
            "supplier": "Dodavatel",
            "expiration_date": "Datum expirace",
            "ean": "EAN",
            "batch": "Šarže",
            "units_in_stock": "Počet jednotek",
            "units_in_package": "Počet jednotek v balení",
            "purchase_price": "Nákupní cena",
            "selling_price": "Prodejní cena",
            "margin": "Marže",
            "note": "Poznámka",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Div("name", css_class="col-span-4"),
                Div("stock", css_class="col-span-1"),
                Div("type", css_class="col-span-1"),
                Div("units_in_package", css_class="col-span-1"),
                Div("units_in_stock", css_class="col-span-1"),
                Div("batch", css_class="col-span-2"),
                Div("ean", css_class="col-span-2"),
                Div("supplier_code", css_class="col-span-1"),
                Div("supplier", css_class="col-span-2"),
                Div("expiration_date", css_class="col-span-2"),
                Div("purchase_price", css_class="col-span-1"),
                Div("margin", css_class="col-span-1"),
                Div("selling_price", css_class="col-span-1"),
                Div("note", css_class="col-span-6"),
                css_class="grid gap-4 grid-cols-6",
            ),
            Submit(
                "submit",
                "Uložit",
                css_class="cursor-pointer text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800",
            ),
        )
