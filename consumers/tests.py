from django.test import TestCase

from .models import Consumer


class UsersManagersTests(TestCase):
    def test_create_user(self):
        user = Consumer.objects.create_user(
            email="test@example.com", password="fooBar123"
        )
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            self.assertIsNone(user.username)
        except ValueError:
            pass

    def test_create_super_user(self):
        user = Consumer.objects.create_superuser(
            email="test@example.com", password="fooBar123"
        )
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
        try:
            self.assertIsNone(user.username)
        except ValueError:
            pass
