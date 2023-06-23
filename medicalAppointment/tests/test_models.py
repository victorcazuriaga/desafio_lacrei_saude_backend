from django.test import TestCase
from registry.models import Doctor, Patient
from medicalAppointment.models import MedicalAppointment, StatusFieldChoices
from datetime import timezone
from model_bakery import baker
from pytz import timezone
from datetime import datetime


class MedicalAppointmentModelTestCase(TestCase):
    def setUp(self):
        self.doctor = baker.make(Doctor)
        self.patient = baker.make(Patient)
        self.current_datetime = datetime.now(timezone("America/Sao_paulo")).strftime(
            "%Y-%m-%dT%H:%M:%SZ"
        )

        self.appointment = MedicalAppointment.objects.create(
            doctor=self.doctor,
            patient=self.patient,
            appointmentDate=self.current_datetime,
            description="Test appointment",
        )

    def test_medical_appointment_tentative_creation(self):
        self.assertEqual(self.appointment.doctor, self.doctor)
        self.assertEqual(self.appointment.patient, self.patient)
        self.assertEqual(self.appointment.description, "Test appointment")
        self.assertEqual(self.appointment.status, StatusFieldChoices.AGENDADO)

    def test_medical_appointment_last_modified(self):
        initial_last_modified = self.appointment.last_modified
        self.appointment.description = "Updated description"
        self.appointment.save()
        self.assertNotEqual(self.appointment.last_modified, initial_last_modified)
