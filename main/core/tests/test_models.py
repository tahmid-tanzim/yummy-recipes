from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTestCase(TestCase):

    def test_create_user_with_email_successfull(self):
        """Ensure we can create a new user object."""
        email = 'test@oneleven.com',
        password = 'Te$t.123',

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a  new user is normalized"""
        email = 'test@ONELEVEN.COM'

        user = get_user_model().objects.create_user(
            email=email,
            password='Te$t.123'
        )

        self.assertEqual(user.email, email.lower())
