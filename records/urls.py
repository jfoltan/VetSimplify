from django.urls import path
from .views import (
    OwnerListView,
    OwnerDetailView,
    OwnerCreateView,
    OwnerUpdateView,
    OwnerDeleteView,
)

app_name = "records"

urlpatterns = [
    path("owners", OwnerListView.as_view(), name="owner_list"),
    path("owners/create", OwnerCreateView.as_view(), name="owner_create"),
    path("owners/<int:pk>", OwnerDetailView.as_view(), name="owner_detail"),
    path("owners/<int:pk>/update", OwnerUpdateView.as_view(), name="owner_update"),
    path("owners/<int:pk>/delete", OwnerDeleteView.as_view(), name="owner_delete"),
]
