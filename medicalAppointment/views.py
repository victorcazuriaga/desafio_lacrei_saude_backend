from django.shortcuts import render
from rest_framework import generics, status
from medicalAppointment.serializers import MedicalAppointmentSerializer
from medicalAppointment.models import MedicalAppointment
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from pytz import timezone
from datetime import datetime


# Create your views here.
class CreateListMedicalAppointment(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = MedicalAppointmentSerializer
    queryset = MedicalAppointment.objects.all()

    def create(self, request, *args, **kwargs):
        appointment_date_str = request.data.get("appointmentDate")
        current_datetime = datetime.now(timezone("America/Sao_Paulo"))

        if appointment_date_str:
            appointment_date = datetime.strptime(
                appointment_date_str, "%Y-%m-%dT%H:%M:%SZ"
            )
            appointment_date = timezone("America/Sao_Paulo").localize(appointment_date)

        if appointment_date and appointment_date < current_datetime:
            return Response(
                {
                    "error": "It is not possible to schedule an appointment with a retroactive date and time."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        return super().create(request, *args, **kwargs)


class ListMedicalAppointmentQuery(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = MedicalAppointmentSerializer
    queryset = MedicalAppointment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["patient_id", "doctor_id", "status"]


class RetriveUpdateDeleteMedicalAppointment(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = MedicalAppointmentSerializer
    queryset = MedicalAppointment.objects.all()
    lookup_url_kwarg = "id"
