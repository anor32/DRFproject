from  rest_framework.test import APITestCase

from sections.models import Section, Content
from sections.tests.utils import get_admin_user, get_member_user
from rest_framework import  status

from sections.urls import section


class ContentTestCase(APITestCase):

    def setUp(self):
        self.user = get_admin_user()
        response = self.client.post('/users/token/', {"email":self.user.email,'password':'qwerty'})
        self.access_token = response.json.get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")
        self.test_section = Section.objects.create(
            title ="Test Section",
            description ="Test Description",
        )
        self.test_content = Content.objects.create(
            section= self.test_section,
            title = 'Test Title',
            content = "Test Content",
            )

    def test_07_content_create(self):
        data = {
            'section':self.test_section.id,
            'title': "Test Title Create",
            "description": "Test Content Create"

        }
        response = self.client.post('/content/create/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json().get('title'), "Test Title Create",)
        self.assertEqual(response.json().get('description'), "Test Content Create")

    def test_08_content_deta(self):
        response = self.client.get(f'/content/{self.test_content.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('title'), "Test Title", )
        self.assertEqual(response.json().get('description'), "Test Content")

    def test_09_content_update(self):
        data = {
            'section':self.test_section.id,
            'title': "Test Title update Patch"
        }
        response = self.client.patch(f'/content/{self.test_content.id}/update/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('title'),  "Test Title update Patch", )

    def test_10_content_delete(self):
        response = self.client.delete(f'/content/{self.test_content.id}/delete/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.delete(f'/content/{self.test_content.id}/delete/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_11_content_list(self):
        response = self.client.get('/content/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['results'][0]['title'], 'Test Title')

    def test_12_content_create_forbidden(self):
        member = get_member_user()
        response = self.client.post(f'/users/token/',{"email":member.email, 'password':'qwerty'})
        self.access_token = response.json().get('access'),
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")

        data = {
            'section': self.test_section.id,
            'title': "Test Title Create",
            "description": "Test Content Create"

        }
        response = self.client.post('/content/create/',data=data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.json().get('detail'), "У вас недостаточно прав для выполнения данного действия")
