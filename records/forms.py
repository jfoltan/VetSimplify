from django import forms
from .models import Owner, Animal, AnimalCase, Visit, VisitStockItem
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div
from django.forms.models import inlineformset_factory


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


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = [
            "name",
            "animal_type",
            "gender",
            "breed",
            "date_of_birth",
            "chip_number",
            "chip_location",
            "chip_application_date",
            "passport_number",
            "passport_issue_date",
            "castration",
            "dead",
            "insured",
            "note",
        ]
        labels = {
            "name": "Jméno",
            "animal_type": "Druh",
            "gender": "Pohlaví",
            "breed": "Plemeno",
            "date_of_birth": "Datum narození",
            "chip_number": "Číslo čipu",
            "chip_location": "Umístění čipu",
            "chip_application_date": "Datum aplikace čipu",
            "passport_number": "Číslo pasu",
            "passport_issue_date": "Datum vydání pasu",
            "castration": "Kastrace",
            "dead": "Uhynulé zvíře",
            "insured": "Pojištěné zvíře",
            "note": "Poznámka",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Div("name", css_class="col-span-1"),
                Div("animal_type", css_class="col-span-1"),
                Div("gender", css_class="col-span-1"),
                Div("breed", css_class="col-span-2"),
                Div("date_of_birth", css_class="col-span-1"),
                Div("chip_number", css_class="col-span-2"),
                Div("chip_location", css_class="col-span-1"),
                Div("chip_application_date", css_class="col-span-1"),
                Div("passport_number", css_class="col-span-1"),
                Div("passport_issue_date", css_class="col-span-1"),
                Div("castration", css_class="col-span-1"),
                Div("dead", css_class="col-span-1"),
                Div("insured", css_class="col-span-1"),
                Div("note", css_class="col-span-6"),
                css_class="grid gap-4 grid-cols-6",
            ),
            Submit(
                "submit",
                "Uložit",
                css_class="cursor-pointer text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800",
            ),
        )


class AnimalCaseForm(forms.ModelForm):
    class Meta:
        model = AnimalCase
        fields = [
            "name",
            "closed",
        ]
        labels = {
            "name": "Název případu",
            "closed": "Uzavřeno",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Div("name", css_class="col-span-4"),
                Div("closed", css_class="col-span-2"),
                css_class="grid gap-4 grid-cols-6",
            ),
            Submit(
                "submit",
                "Uložit",
                css_class="cursor-pointer text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800",
            ),
        )


class VisitStockItemForm(forms.ModelForm):
    class Meta:
        model = VisitStockItem
        fields = [
            "stock_item",
            "quantity",
            "price",
        ]
        labels = {
            "stock_item": "Položka skladu",
            "quantity": "Množství",
            "price": "Cena",
        }


VisitFormSet = inlineformset_factory(
    Visit,
    VisitStockItem,
    form=VisitStockItemForm,
    extra=0,
    can_delete=False,
    fields=("stock_item", "quantity", "price"),
)


class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = [
            "weight",
            "temperature",
            "record",
        ]
        labels = {
            "weight": "Hmotnost",
            "temperature": "Teplota",
            "record": "Záznam",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.disable_csrf = True
        self.helper.layout = Layout(
            Div(
                Div("weight", css_class="col-span-1"),
                Div("temperature", css_class="col-span-1"),
                Div("record", css_class="col-span-6"),
                css_class="grid gap-4 grid-cols-6",
            ),
        )
