from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class AuthenticationTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_signup(self):
        # Test signup functionality
        print("Testing signup functionality...")
        response = self.client.post(reverse('account:register'), {
            'username': 'test_user',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'test@example.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123'
        })
        print("Signup response:", response)
        self.assertEqual(response.status_code, 302)
        print("302 success redirected")
        self.assertTrue(User.objects.filter(username='test_user').exists())
        print("Signup successful.")

    def test_login(self):
        # Test login functionality
        print("Testing login functionality...")
        User.objects.create_user(username='test_user', password='testpassword123')
        response = self.client.post(reverse('account:login'), {
            'username': 'test_user',
            'password': 'testpassword123'
        })
        print("Login response:", response)
        self.assertEqual(response.status_code, 302)
        self.assertTrue('_auth_user_id' in self.client.session)
        print("Login successful.")

    def test_logout(self):
        # Test logout functionality
        print("Testing logout functionality...")
        User.objects.create_user(username='test_user', password='testpassword123')
        self.client.login(username='test_user', password='testpassword123')
        response = self.client.get(reverse('account:logout'))
        print("Logout response:", response)
        self.assertEqual(response.status_code, 302)
        self.assertFalse('_auth_user_id' in self.client.session)
        print("Logout successful.")
