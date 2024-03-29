from django.shortcuts import render
from .models import Stock, StockItem
from .forms import StockItemForm, StockForm
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@login_required
def stock(request, stock_id=None):
    items = StockItem.objects.all()

    # Filtrace podle skladu, pokud je zvolen
    if stock_id is not None:
        items = items.filter(stock_id=stock_id)

    # Filtrace podle typu, pokud je zvolen
    type = request.GET.get("type")
    if type:
        items = items.filter(type=type)

    stocks = Stock.objects.all()

    unique_types = set(item.type for item in StockItem.objects.all())

    # Převod kódů typů na lidsky čitelné hodnoty
    type_choices_dict = dict(StockItem.TYPE_CHOICES)
    types = {
        unique_type: type_choices_dict[unique_type] for unique_type in unique_types
    }

    page = request.GET.get("page", 1)
    paginator = Paginator(items, 10)
    try:
        items_paged = paginator.page(page)
    except PageNotAnInteger:
        items_paged = paginator.page(1)
    except EmptyPage:
        items_paged = paginator.page(paginator.num_pages)

    context = {
        "items_paged": items_paged,
        "items": items,
        "stocks": stocks,
        "choosen_stock": stock_id,
        "types": types,
        "choosen_type": type,
    }

    return render(request, "stock/stock_items.html", context)


class StockCreateView(LoginRequiredMixin, CreateView):
    model = Stock
    form_class = StockForm
    template_name = "stock/stock_form.html"

    def get_success_url(self):
        return reverse("stock:stock")


class StockItemCreateView(LoginRequiredMixin, CreateView):
    model = StockItem
    form_class = StockItemForm
    template_name = "stock/stock_item_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["stocks"] = Stock.objects.all()
        return context

    def get_success_url(self):
        return reverse("stock:stock")


class StockItemUpdateView(LoginRequiredMixin, UpdateView):
    model = StockItem
    form_class = StockItemForm
    template_name = "stock/stock_item_update_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["stocks"] = Stock.objects.all()
        return context

    def get_success_url(self):
        return reverse("stock:stock")


class StockItemDeleteView(LoginRequiredMixin, DeleteView):
    model = StockItem

    def get_success_url(self):
        return reverse("stock:stock")
