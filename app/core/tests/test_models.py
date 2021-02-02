from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelsTest(TestCase):

    def test_create_new_user_with_email_successful(self):
        """Test if a new user with email is created successfully"""
        email = 'johann@wondrouswebworks.dev'
        password = 'Testing123'

        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))