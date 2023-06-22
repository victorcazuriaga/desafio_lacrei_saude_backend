from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken
from . import views

urlpatterns = [
    path('register', views.CreateListUserView.as_view()),
    path('login', ObtainAuthToken.as_view())
]
