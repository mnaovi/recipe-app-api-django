from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_model_successful(self):
        """create a user with email"""
        email = 'nazmul@gmail.com'
        password = 'hello123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """create a user with normalized email"""
        email = 'hello@GMAIL.COM'
        user = get_user_model().objects.create_user(email, 'tress122')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'lkjlkjj')

    def test_create_new_superuser(self):
        """Test creating new superuser"""
        user = get_user_model().objects.create_superuser(
            'hello@gmail.com',
            'jkljkljlkj'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
