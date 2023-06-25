from django.test import TestCase
from model_bakery import baker
# Create your tests here.
class UserModelTest(TestCase):
    def setUp(self):
         self.user_1 = baker.make("users.User")
         self.user_2 = baker.make("users.User")

    def test_create_user (self):
        user = self.user_1
        self.assertIsNotNone(user.username)
        self.assertIsNotNone(user.password)

    