from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from registry.models import Doctor
from registry.serializers import DoctorSerializer


class CreateDoctorViewTestCase(TestCase):
    @classmethod
    def setUp(cls):
        super().setUp()
        cls.client = APIClient()

        cls.url = reverse("doctor-list")

        cls.valid_payload = {
            "socialName": "Dr. Fulano",
            "name": "Fulano",
            "lastName": "de Tal",
            "email": "fulano@example.com",
            "cpf": "12345678901",
            "rg": "1234567",
            "crm": "123456",
            "medicalSpecialty": "Cardiologia",
            "birthdate": "1990-01-01",
            "address": {
                "street": "Rua Principal",
                "number": "123",
                "district": "Cidade",
                "state": "Estado",
                "zipcode": "12345678",
            },
            "comments": "Comentários sobre o médico",
        }
        cls.invalid_payload = {
            # Preencha os dados inválidos conforme necessário
        }

        cls.user = {"username": "user_test", "password": "password_test"}

        cls.client.post("/api/register", data=cls.user, format="json")
        response = cls.client.post("/api/login", data=cls.user, format="json")
        cls.token = response.data["token"]

    def test_create_doctor_valid_payload(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token)
        response = self.client.post(self.url, data=self.valid_payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_doctor_invalid_payload(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token)
        response = self.client.post(self.url, data=self.invalid_payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class RetriveUpdateDestroyDoctorViewTestCase(TestCase):
    @classmethod
    def setUp(cls):
        super().setUp()
        cls.client = APIClient()

        cls.valid_payload = {
            "socialName": "Dr. Fulano",
            "name": "Fulano",
            "lastName": "de Tal",
            "email": "fulano@example.com",
            "cpf": "12345678901",
            "rg": "1234567",
            "crm": "123456",
            "medicalSpecialty": "Cardiologia",
            "birthdate": "1990-01-01",
            "address": {
                "street": "Rua Principal",
                "number": "123",
                "district": "Cidade",
                "state": "Estado",
                "zipcode": "12345678",
            },
            "comments": "Comentários sobre o médico",
        }
        cls.invalid_payload = {
            # Preencha os dados inválidos conforme necessário
        }

        cls.doctor = Doctor.objects.create(**cls.valid_payload)

    def setUp(self):
        self.client.force_authenticate(user=None)

    def test_retrieve_doctor(self):
        url = reverse("doctor-detail", kwargs={"id": self.doctor.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_doctor_valid_payload(self):
        url = reverse("doctor-detail", kwargs={"id": self.doctor.id})
        response = self.client.put(url, data=self.valid_payload)
