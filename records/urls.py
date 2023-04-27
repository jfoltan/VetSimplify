from django.urls import path
from .views import (
    OwnerListView,
    OwnerDetailView,
    OwnerCreateView,
    OwnerUpdateView,
    OwnerDeleteView,
    AnimalCreateView,
    AnimalDetailView,
    AnimalUpdateView,
    AnimalDeleteView,
)

app_name = "records"

urlpatterns = [
    # Owners URLs
    path("owners", OwnerListView.as_view(), name="owner_list"),
    path("owners/create", OwnerCreateView.as_view(), name="owner_create"),
    path("owners/<int:owner_id>", OwnerDetailView.as_view(), name="owner_detail"),
    path(
        "owners/<int:owner_id>/update", OwnerUpdateView.as_view(), name="owner_update"
    ),
    path(
        "owners/<int:owner_id>/delete", OwnerDeleteView.as_view(), name="owner_delete"
    ),
    # Animals URLs
    path(
        "owners/<int:owner_id>/animals/create",
        AnimalCreateView.as_view(),
        name="animal_create",
    ),
    path(
        "owners/<int:owner_id>/animals/<int:animal_id>",
        AnimalDetailView.as_view(),
        name="animal_detail",
    ),
    path(
        "owners/<int:owner_id>/animals/<int:animal_id>/update",
        AnimalUpdateView.as_view(),
        name="animal_update",
    ),
    path(
        "owners/<int:owner_id>/animals/<int:animal_id>/delete",
        AnimalDeleteView.as_view(),
        name="animal_delete",
    ),
]
