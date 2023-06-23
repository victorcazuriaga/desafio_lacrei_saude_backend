from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path(
        "appointment",
        views.CreateListMedicalAppointment.as_view(),
        name="appointment-create",
    ),
    path(
        "appointments",
        views.ListMedicalAppointmentQuery.as_view(),
        name="appointment-list-query",
    ),
    path(
        "appointment/<str:id>",
        views.RetriveUpdateDeleteMedicalAppointment.as_view(),
        name="appointment-details",
    ),
]
