# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from registry.models import Doctor, Patient
from medicalAppointment.models import MedicalAppointment, StatusFieldChoices
from medicalAppointment.serializers import MedicalAppointmentSerializer
from medicalAppointment.views import (
    CreateListMedicalAppointment,
    ListMedicalAppointmentQuery,
)


class MedicalAppointmentViewTestCase(TestCase):
    @classmethod
    def setUp(cls):
        cls.client = APIClient()
        cls.doctor = Doctor.objects.create(name="Dr. John Doe")
        cls.patient = Patient.objects.create(name="Alice")

        cls.user = {"username": "user_test", "password": "password_test"}
        cls.client.post("/api/register", data=cls.user, format="json")
        response = cls.client.post("/api/login", data=cls.user, format="json")
        cls.token = response.data["token"]

    def test_create_medical_appointment_with_future_date(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token)
        url = reverse("appointment-list")
        appointment_data = {
            "doctor": self.doctor.id,
            "patient": self.patient.id,
            "description": "Test appointment",
            "appointmentDate": "2023-06-25T10:00:00Z",
            "status": StatusFieldChoices.AGENDADO,
        }
        request = self.client.post(url, appointment_data)
        response = CreateListMedicalAppointment.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            MedicalAppointment.objects.first().status, StatusFieldChoices.AGENDADO
        )

    def test_create_medical_appointment_with_past_date(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token)
        url = reverse("appointment-create")
        appointment_data = {
            "doctor": self.doctor.id,
            "patient": self.patient.id,
            "description": "Test appointment",
            "appointmentDate": "2022-06-20T10:00:00Z",
            "status": StatusFieldChoices.AGENDADO,
        }
        request = self.client.post(url, appointment_data)
        response = CreateListMedicalAppointment.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(MedicalAppointment.objects.count(), 0)

    def test_list_medical_appointments_with_filters(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token)
        MedicalAppointment.objects.create(
            doctor=self.doctor,
            patient=self.patient,
            description="Test appointment 1",
            appointmentDate="2023-06-20T10:00:00Z",
            status=StatusFieldChoices.AGENDADO,
        )
        MedicalAppointment.objects.create(
            doctor=self.doctor,
            patient=self.patient,
            description="Test appointment 2",
            appointmentDate="2023-06-25T10:00:00Z",
            status=StatusFieldChoices.CONCLUIDO,
        )
        url = reverse("appointments-create")
        request = self.client.get(url, {"status": StatusFieldChoices.AGENDADO})
        response = ListMedicalAppointmentQuery.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
