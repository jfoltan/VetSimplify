from django.urls import path
from .views import stock, StockItemCreateView, StockItemUpdateView, StockItemDeleteView

app_name = "stock"

urlpatterns = [
    path("", stock, name="stock"),
    path("<int:stock_id>", stock, name="stock_items_by_stock"),
    path("item_create", StockItemCreateView.as_view(), name="stock_item_create"),
    path(
        "item_update/<int:pk>", StockItemUpdateView.as_view(), name="stock_item_update"
    ),
    path(
        "item_delete/<int:pk>", StockItemDeleteView.as_view(), name="stock_item_delete"
    ),
    # path("item/<int:item_id>", item_detail, name="item_detail"),
]
