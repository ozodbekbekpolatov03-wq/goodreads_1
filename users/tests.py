# from django.contrib.auth import get_user_model
# from django.test import Client, TestCase
# from django.urls import reverse


# class UserAuthTests(TestCase):
#     def test_register_creates_hashed_user(self):
#         client = Client()

#         response = client.post(
#             reverse('register'),
#             {
#                 'username': 'alice',
#                 'first_name': 'Alice',
#                 'last_name': 'Example',
#                 'email': 'alice@example.com',
#                 'password': 'StrongPass123',
#             },
#         )

#         self.assertEqual(response.status_code, 302)
#         user = get_user_model().objects.get(username='alice')
#         self.assertTrue(user.check_password('StrongPass123'))
#         self.assertNotEqual(user.password, 'StrongPass123')

#     def test_login_authenticates_existing_user(self):
#         user = get_user_model().objects.create_user(
#             username='bob',
#             email='bob@example.com',
#             password='StrongPass123',
#         )
#         client = Client()

#         response = client.post(
#             reverse('login'),
#             {'username': 'bob', 'password': 'StrongPass123'},
#         )

#         self.assertEqual(response.status_code, 302)
#         self.assertTrue(response.wsgi_request.user.is_authenticated)

from django.contrib.auth.models import User
from django.test import  TestCase
from django.urls import reverse

class RegstirationTestCase(TestCase):
    def test_user_account_is_created(self):
        self.client.post(reverse('register'), 
                        data={
                            'username': 'testuser',
                            'email': 'testuser@example.com',
                            'first_name': 'Test',
                            'last_name': 'User',
                            'password': 'TestPass123'
                        })
        user=User.objects.get(username='testuser')
        self.assertEqual(user.first_name, 'Test')
        self.assertEqual(user.last_name, 'User')
        self.assertEqual(user.email, 'testuser@example.com')
        self.assertNotEqual(user.password, 'TestPass123')  
        self.assertTrue(user.check_password("TestPass123"))

    def test_required_fields(self):
        response=self.client.post(
            reverse("register"),
            data={
                'first_name': 'Test',
                'email': 'testuser@example.com',
            }
        )
        user_count=User.objects.count()
        self.assertEqual(user_count, 0)
        # self.assertFormError(response, "form", "username", "This field is required.")
        # self.assertFormError(response, "form", "password", "This field is required.")
                
   