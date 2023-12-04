from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from ads.models import Ad
from users.models import User


class UserViewSetTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(email='TestUser@Test.com', first_name='Test', phone='+19430292',
                                             last_name='User')
        self.user.set_password('TestPassword')
        self.user.save()
        self.client.force_authenticate(user=self.user)

    def tearDown(self):
        self.user.delete()

    def test_user_create(self):
        response = self.client.post(reverse('users:users-list'), data={
            'email': 'test@gmail.com',
            'first_name': 'test',
            'last_name': 'test',
            'phone': '+998909090909',
            'password': 'testqwerty',
            're_password': 'testqwerty',
            'role': 'user', }
                                    )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(), {
            'id': self.user.pk + 1,
            'email': 'test@gmail.com',
            'first_name': 'test',
            'last_name': 'test',
            'phone': '+998909090909',
            'role': 'user',
        })

    def test_user_update(self):
        response = self.client.patch(reverse('users:users-detail', args=(self.user.pk,)), data={
            'first_name': 'test updated',
            'last_name': 'test updated'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {
            'first_name': 'test updated',
            'last_name': 'test updated',
            'phone': '+19430292',
            'role': 'user',
            'id': self.user.pk,
            'email': 'TestUser@test.com'
        })

    def test_get_user_list(self):
        # List of users only will display to admin
        self.staff_user = User.objects.create_superuser(email='stuff@test@gmail.com', first_name='stuff',
                                                        phone='+998909090909', last_name='stuff', role='admin')
        self.staff_user.set_password('stuffqwerty')
        self.staff_user.save()
        self.client.force_authenticate(user=self.staff_user)
        response = self.client.get(reverse('users:users-list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(),
                         {'count': 2,
                          'next': None,
                          'previous': None,
                          'results': [
                              {'first_name': 'stuff',
                               'last_name': 'stuff',
                               'phone': '+998909090909',
                               'role': 'admin',
                               'id': 2,
                               'email': 'stuff@test@gmail.com'},

                              {'first_name': 'Test',
                               'last_name': 'User',
                               'phone': '+19430292',
                               'role': 'user',
                               'id': 1,
                               'email': 'TestUser@test.com'}]})

    def test_get_user_list_by_user(self):
        # List of users only will display to admin other than that will return current user
        request = self.client.get(reverse('users:users-list'))
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(request.json(), {
            'count': 1,
            'next': None,
            'previous': None,
            'results': [
                {'first_name': 'Test',
                 'last_name': 'User',
                 'phone': '+19430292',
                 'role': 'user',
                 'id': 3,
                 'email': 'TestUser@test.com'}]})

    def test_user_delete(self):
        response = self.client.delete(reverse('users:users-detail', args=(self.user.pk,)), data={
            'current_password': 'TestPassword'
        })
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
