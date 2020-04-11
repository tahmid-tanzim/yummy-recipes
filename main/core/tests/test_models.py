from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTestCase(TestCase):

    def test_create_user_with_email_successfull(self):
        """Ensure we can create a new user object."""

        email = 'test@oneleven.com'
        password = 'Te$t.123'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a  new user is normalized"""

        email = 'test@ONELEVEN.COM'
        password = 'Te$t.123'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'Te$t.123')

    def test_create_new_superuser(self):
        """Test creating a  new superuser"""

        email = 'test@ONELEVEN.COM'
        password = 'Te$t.123'

        user = get_user_model().objects.create_superuser(
            email=email,
            password=password
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
