from django import forms
from .models import Owner
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div


class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = [
            "first_name",
            "last_name",
            "street",
            "house_number",
            "city",
            "postal_code",
            "country",
            "phone_number",
            "email",
            "company_name",
            "ic",
            "dic",
            "note",
        ]
        labels = {
            "first_name": "Jméno",
            "last_name": "Příjmení",
            "street": "Ulice",
            "house_number": "Č. p.",
            "city": "Město",
            "postal_code": "PSČ",
            "country": "Země",
            "phone_number": "Telefon",
            "email": "E-mail",
            "company_name": "Název firmy",
            "ic": "IČ",
            "dic": "DIČ",
            "note": "Poznámka",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Div("first_name", css_class="col-span-3"),
                Div("last_name", css_class="col-span-3"),
                Div("street", css_class="col-span-2"),
                Div("house_number", css_class="col-span-1"),
                Div("city", css_class="col-span-2"),
                Div("postal_code", css_class="col-span-1"),
                Div("country", css_class="col-span-2"),
                Div("phone_number", css_class="col-span-2"),
                Div("email", css_class="col-span-2"),
                Div("company_name", css_class="col-span-2"),
                Div("ic", css_class="col-span-1"),
                Div("dic", css_class="col-span-1"),
                Div("note", css_class="col-span-6"),
                css_class="grid gap-4 grid-cols-6",
            ),
            Submit(
                "submit",
                "Uložit",
                css_class="cursor-pointer text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800",
            ),
        )
