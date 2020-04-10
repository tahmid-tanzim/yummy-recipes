from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTestCase(TestCase):

    def test_create_user_with_email_successfull(self):
        """Ensure we can create a new user object."""
        username = 'test_user',
        email = 'test@oneleven.com',
        password = 'Te$t.123',

        user = get_user_model().objects.create_user(
            username=username,
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertEqual(user.username, username)
        self.assertTrue(user.check_password(password))

