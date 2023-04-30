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
    AnimalCaseCreateView,
    AnimalCaseDetailView,
    AnimalCaseUpdateView,
    AnimalCaseDeleteView,
    VisitCreateView,
    VisitUpdateView,
    VisitDeleteView,
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
    # AnimalCase URLs
    path(
        "owners/<int:owner_id>/animals/<int:animal_id>/cases/create",
        AnimalCaseCreateView.as_view(),
        name="animal_case_create",
    ),
    path(
        "owners/<int:owner_id>/animals/<int:animal_id>/cases/<int:animalcase_id>",
        AnimalCaseDetailView.as_view(),
        name="animal_case_detail",
    ),
    path(
        "owners/<int:owner_id>/animals/<int:animal_id>/cases/<int:animalcase_id>/update",
        AnimalCaseUpdateView.as_view(),
        name="animal_case_update",
    ),
    path(
        "owners/<int:owner_id>/animals/<int:animal_id>/cases/<int:animalcase_id>/delete",
        AnimalCaseDeleteView.as_view(),
        name="animal_case_delete",
    ),
    # Visit URLs
    path(
        "owners/<int:owner_id>/animals/<int:animal_id>/cases/<int:animalcase_id>/visits/create",
        VisitCreateView.as_view(),
        name="visit_create",
    ),
    path(
        "owners/<int:owner_id>/animals/<int:animal_id>/cases/<int:animalcase_id>/visits/<int:visit_id>/update",
        VisitUpdateView.as_view(),
        name="visit_update",
    ),
    path(
        "owners/<int:owner_id>/animals/<int:animal_id>/cases/<int:animalcase_id>/visits/<int:visit_id>/delete",
        VisitDeleteView.as_view(),
        name="visit_delete",
    ),
]
