from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_success(self):
        '''Testing creating a user with new email'''

        email = 'test123@gmail.com'
        password = 'Testpass123'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_user_with_email_normalized(self):
        '''Testing creating a user with normalized email'''

        email = 'test123@GMAIL.COM'
        password = 'Testpass123'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        '''creating user with invalid email should raise error'''

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'avc123')

    def test_create_super_user(self):
        '''creating super user'''

        user = get_user_model().objects.create_superuser('test123@gmail.com', 'Test123')

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
