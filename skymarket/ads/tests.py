from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from ads.models import Ad
from users.models import User


class AdViewSetTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = User.objects.create_user(email='TestUser@Test.com', first_name='Test', phone='+19430292',
                                             last_name='User')
        self.user.set_password('TestPassword')
        self.user.save()

        self.ad = Ad.objects.create(title='Test Ad', price='1000', description='Test Description', author=self.user)

        self.client.force_authenticate(user=self.user)

    def tearDown(self):
        self.user.delete()
        self.ad.delete()

    def test_ad_creation_by_authenticated_user(self):
        response = self.client.post(reverse('ads:ads-list'), data={
            'title': 'Test Ad 2',
            'price': '2000',
            'description': 'Test Description 2',
            'author': self.user.pk,

        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Test Ad 2')

    def test_ad_creation_by_unauthenticated_user(self):
        self.client.logout()
        response = self.client.post(reverse('ads:ads-list'), data={
            'title': 'Test Ad 2',
            'price': '2000',
            'description': 'Test Description 2',
            'author': self.user.pk,

        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_ad_update_by_authenticated_user(self):
        response = self.client.patch(reverse('ads:ads-detail', args=(self.ad.pk,)), data={
            'title': 'Test Ad 2',
            'price': '2000',
            'description': 'Test Description 2',
            'author': self.user.pk,

        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Ad 2')

    def test_ad_update_by_unauthenticated_user(self):
        self.client.logout()
        response = self.client.patch(reverse('ads:ads-detail', args=(self.ad.pk,)), data={
            'title': 'Test Ad 2',
            'price': '2000',
            'description': 'Test Description 2',
            'author': self.user.pk,

        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_ad_delete_by_authenticated_user(self):
        response = self.client.delete(reverse('ads:ads-detail', args=(self.ad.pk,)))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_ad_delete_by_unauthenticated_user(self):
        self.client.logout()
        response = self.client.delete(reverse('ads:ads-detail', args=(self.ad.pk,)))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_ad_list_by_authenticated_user(self):
        response = self.client.get(reverse('ads:ads-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(),
                         {'count': 1,
                          'next': None,
                          'previous': None,
                          'results': [
                              {'id': self.ad.pk,
                               'author': 'TestUser@test.com',
                               'title': 'Test Ad',
                               'price': 1000,
                               'description': 'Test Description',
                               'created_at': self.ad.created_at.strftime('%Y-%m-%dT%H:%M:%S.%fZ')}]})

    def test_ad_list_by_unauthenticated_user(self):
        # Unauthenticated users can see ads list
        self.client.logout()
        response = self.client.get(reverse('ads:ads-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_ad_detail_by_authenticated_user(self):
        response = self.client.get(reverse('ads:ads-detail', args=(self.ad.pk,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {
            'pk': self.ad.pk,
            'title': 'Test Ad',
            'price': 1000,
            'description': 'Test Description',
            'phone': '+19430292',
            'author': 'TestUser@test.com',
            'author_first_name': 'Test',
            'author_last_name': 'User',
            'author_id': self.user.pk,
        })

    def test_ad_detail_by_unauthenticated_user(self):
        # Unauthenticated users can see ads detail
        self.client.logout()
        response = self.client.get(reverse('ads:ads-detail', args=(self.ad.pk,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {
            'pk': self.ad.pk,
            'title': 'Test Ad',
            'price': 1000,
            'description': 'Test Description',
            'phone': '+19430292',
            'author': 'TestUser@test.com',
            'author_first_name': 'Test',
            'author_last_name': 'User',
            'author_id': self.user.pk,
        })

    def test_ad_list_filter_by_title(self):
        response = self.client.get(reverse('ads:ads-list'), data={'title': 'Test Ad'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()['results']), 1)
