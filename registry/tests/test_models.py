from django.test import TestCase
from registry.models import Doctor, Address, Patient
from datetime import date
import ipdb
# Create your tests here.

class DoctorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.address = Address.objects.create(street="Rua Principal", number="123", district="Cidade", state="Estado", zipcode="12345678")
        cls.doctor = Doctor.objects.create(
            socialName="Dr. Fulano",
            name="Fulano",
            lastName="de Tal",
            email="fulano@example.com",
            cpf="12345678901",
            rg="1234567",
            crm="123456",
            medicalSpecialty="Cardiologia",
            birthdate="1990-01-01",
            is_active=True,
            address=cls.address,
            comments="Comentários sobre o médico"
        )

    def test_doctor_creation(self):
        doctor = Doctor.objects.get(id=self.doctor.id)
        self.assertEqual(doctor.socialName, "Dr. Fulano")
        self.assertEqual(doctor.name, "Fulano")
        self.assertEqual(doctor.lastName, "de Tal")
        self.assertEqual(doctor.email, "fulano@example.com")
        self.assertEqual(doctor.cpf, "12345678901")
        self.assertEqual(doctor.rg, "1234567")
        self.assertEqual(doctor.crm, "123456")
        self.assertEqual(doctor.medicalSpecialty, "Cardiologia")
        self.assertEqual(doctor.birthdate,  date(1990, 1, 1))
        self.assertTrue(doctor.is_active)
        self.assertEqual(doctor.address, self.address)
        self.assertEqual(doctor.comments, "Comentários sobre o médico")

    def test_doctor_str_representation(self):
        doctor = Doctor.objects.get(id=self.doctor.id)
        expected_str = f"{doctor.name}, {doctor.lastName}, ({doctor.crm})"
        self.assertEqual(str(doctor), expected_str)

    def test_doctor_unique_fields(self):
        invalid_doctor = Doctor(
            socialName="Dr. Fulano",
            name="Fulano",
            lastName="de Tal",
            email="fulano@example.com",
            cpf="12345678901",
            rg="1234567",
            crm="123456",
            medicalSpecialty="Cardiologia",
            birthdate="1990-01-01",
            is_active=True,
            address=self.address,
            comments="Comentários sobre o médico"
        )
        with self.assertRaises(Exception):
            invalid_doctor.save()

    def test_doctor_address_cascade_deletion(self):
        doctor = Doctor.objects.get(id=self.doctor.id)
        address = doctor.address
        doctor_d = Doctor.objects.get(id=self.doctor.id).delete()
        self.assertFalse(Doctor.objects.filter(id=self.doctor.id).exists())
        self.assertFalse(Address.objects.filter(id=address.id).exists())


class PatientModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.address = Address.objects.create(street="Rua Principal", number="123", district="Cidade", state="Estado", zipcode="12345678")
        cls.patient = Patient.objects.create(
            socialName="Dr. Fulano",
            name="Fulano",
            lastName="de Tal",
            email="fulano@example.com",
            cpf="12345678901",
            rg="1234567",
            birthdate="1990-01-01",
            address=cls.address,
            comments="Comentários sobre o paciente"
        )

    def test_patient_creation(self):
        patient = Patient.objects.get(id=self.patient.id)
        self.assertEqual(patient.socialName, "Dr. Fulano")
        self.assertEqual(patient.name, "Fulano")
        self.assertEqual(patient.lastName, "de Tal")
        self.assertEqual(patient.email, "fulano@example.com")
        self.assertEqual(patient.cpf, "12345678901")
        self.assertEqual(patient.rg, "1234567")
        self.assertEqual(patient.birthdate, date(1990, 1, 1))
        self.assertTrue(patient.is_active)
        self.assertEqual(patient.address, self.address)
        self.assertEqual(patient.comments, "Comentários sobre o paciente")

    def test_patient_str_representation(self):
        patient = Patient.objects.get(id=self.patient.id)
        expected_str = f"{patient.name}, {patient.lastName}, {patient.cpf}"
        self.assertEqual(str(patient), expected_str)

    def test_patient_unique_fields(self):
        invalid_patient = Patient(
            socialName="Dr. Fulano",
            name="Fulano",
            lastName="de Tal",
            email="fulano@example.com",
            cpf="12345678901",
            rg="1234567",
            birthdate="1990-01-01",
            address=self.address,
            comments="Comentários sobre o paciente"
        )
        with self.assertRaises(Exception):
            invalid_patient.save()

    def test_patient_address_cascade_deletion(self):
        patient = Patient.objects.get(id=self.patient.id)
        address = patient.address
        patient.delete()
        self.assertFalse(Patient.objects.filter(id=self.patient.id).exists())
        self.assertFalse(Address.objects.filter(id=address.id).exists())