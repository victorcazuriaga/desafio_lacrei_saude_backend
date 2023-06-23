from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    #------------------- Doctor Routes -----------------------
    path('doctor', views.CreateDoctorView.as_view(), name="doctor-list"),
    path('doctor/<str:id>', views.RetriveUpdateDestroyDoctorView.as_view(), name="doctor-detail"),

    #------------------- Patient Routes -----------------------
    path('patient', views.CreatePatientView.as_view()),
    path('patient/<str:id>', views.RetriveUpdateDestroyPatientView.as_view()),
    

]
