from rest_framework.test import APITestCase
from users.models import User
from django.test import Client
import ipdb
class UserViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user_data = {"username": "victorCazuriaga", "password": "victor1234"}
        cls.client = Client()

    def test_register_user(cls):
         response_register = cls.client.post('/api/register', cls.user_data, format="json")
         cls.assertEqual(response_register.status_code, 201)

    def test_register_user_exists(cls):
         response_register = cls.client.post('/api/register', cls.user_data, format="json")
         response_register2 = cls.client.post('/api/register', cls.user_data, format="json")
         cls.assertEqual(response_register2.status_code, 400)

    def test_register_user_without_password(cls):
         response_register = cls.client.post('/api/register', cls.user_data["username"], format="json")
         cls.assertEqual(response_register.status_code, 400)
    
    def test_register_user_without_username(cls):
         response_register = cls.client.post('/api/register', cls.user_data["password"], format="json")
         cls.assertEqual(response_register.status_code, 400)

    def test_login_user(cls):
         response_register = cls.client.post('/api/register', cls.user_data, format="json")
         response_login = cls.client.post('/api/login', cls.user_data, format="json")
         cls.assertEqual(response_login.status_code, 200)
    
    def test_login_user_credential_incorrent(cls):
         cls.user_data['password'] = "outraSenha"
         response_login = cls.client.post('/api/login', cls.user_data, format="json")
         cls.assertEqual(response_login.status_code, 400)
         
