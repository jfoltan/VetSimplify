from django import forms
from .models import Procedure
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div


class ProcedureForm(forms.ModelForm):
    class Meta:
        model = Procedure
        fields = ["name", "price", "note"]
        labels = {
            "name": "Název",
            "price": "Cena",
            "note": "Poznámka",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Div("name", css_class="col-span-4"),
                Div("price", css_class="col-span-2"),
                Div("note", css_class="col-span-6"),
                css_class="grid grid-cols-6 gap-4",
            ),
            Submit(
                "submit",
                "Uložit",
                css_class="cursor-pointer text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800",
            ),
        )
