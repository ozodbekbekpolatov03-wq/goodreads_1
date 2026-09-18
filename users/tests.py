from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse


class UserAuthTests(TestCase):
    def test_register_creates_hashed_user(self):
        client = Client()

        response = client.post(
            reverse('register'),
            {
                'username': 'alice',
                'first_name': 'Alice',
                'last_name': 'Example',
                'email': 'alice@example.com',
                'password': 'StrongPass123',
            },
        )

        self.assertEqual(response.status_code, 302)
        user = get_user_model().objects.get(username='alice')
        self.assertTrue(user.check_password('StrongPass123'))
        self.assertNotEqual(user.password, 'StrongPass123')

    def test_login_authenticates_existing_user(self):
        user = get_user_model().objects.create_user(
            username='bob',
            email='bob@example.com',
            password='StrongPass123',
        )
        client = Client()

        response = client.post(
            reverse('login'),
            {'username': 'bob', 'password': 'StrongPass123'},
        )

        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.wsgi_request.user.is_authenticated)
