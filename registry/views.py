from django.shortcuts import render
from .models import Doctor, Patient, Address
from .serializers import DoctorSerializer, AddressSerializer, PatientSerializer
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication 
from rest_framework.permissions import IsAuthenticated
# Create your views here.

# ------------------Doctor Views --------------------------------
class CreateDoctorView (generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()

class RetriveUpdateDestroyDoctorView (generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
    lookup_field = "id"


# ------------------Patient Views --------------------------------

class CreatePatientView (generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

class RetriveUpdateDestroyPatientView (generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()
    lookup_field = "id"

    