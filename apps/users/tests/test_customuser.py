from django.contrib.auth import get_user_model
from django.test import TestCase

class CustomUserTest(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
                username="wil",
                email="will@email.com",
                password='testpass123',
                tin='12345X',
                fiscal_address='St. Nothing',
                phone='123456789',
                lat=1.41,
                lon=1.51,
                description='Some weird description',
                country='ES',
        )
        self.assertEqual(user.username, 'wil')
        self.assertEqual(user.email, 'will@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertEqual(user.tin, '12345X')
        self.assertEqual(user.fiscal_address, 'St. Nothing')
        self.assertEqual(user.phone, '123456789')
        self.assertEqual(user.lat, 1.41)
        self.assertEqual(user.lon, 1.51)
        self.assertIn('weird', user.description)
        self.assertEqual(user.country, 'ES')
        
    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
                username="admin",
                email="admin@email.com",
                password='testpass123',
                tin='012345X',
                fiscal_address='St. Nothing',
                phone='123456789',
                lat=1.41,
                lon=1.51,
                description='Some weird description',
                country='ES',
        )
        self.assertEqual(user.username, 'admin')
        self.assertEqual(user.email, 'admin@email.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
        self.assertEqual(user.tin, '012345X')
        self.assertEqual(user.fiscal_address, 'St. Nothing')
        self.assertEqual(user.phone, '123456789')
        self.assertEqual(user.lat, 1.41)
        self.assertEqual(user.lon, 1.51)
        self.assertIn('weird', user.description)
        self.assertEqual(user.country, 'ES')
     
