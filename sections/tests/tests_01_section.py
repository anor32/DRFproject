from  rest_framework.test import APITestCase

from sections.models import Section
from sections.tests.utils import get_admin_user, get_member_user
from rest_framework import  status

class SectionTestCase(APITestCase):

    def setUp(self):
        self.user = get_admin_user()
        response = self.client.post('/users/token/',
        {"email":"tester@test1.com",'password':'qwerty'})
        self.access_token = response.json.get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")
        self.test_section = Section.objects.create(
            title ="Test Section",
            description ="Test Description",
        )

    def test_01_section_create(self):
        data = {
            'title': "Test Section Create",
            "description": "Test Description Create"

        }
        response = self.client.post('section/create/',data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json().get('title'), "Test Section Create")
        self.assertEqual(response.json().get('description'), "Test Description Create")
        print(response.json())

    def test_02_section_detail(self):
        response = self.client.get('/section/3/')
        # print(response.json())
        self.assertEqual(response.status_code_code,status.HTTP_200_OK)
        self.assertEqual(response.json().get('title'), "Test Section")
        self.assertEqual(response.json().get('description'), "Test Description")

    def test_03_section_update(self):
        data = {
            'title' : "Test Section Update Put",
            'description' : "Test Section Description Put",
        }
        response = self.client.put(f'/section/{self.test_section.id}/update')
        self.assertEqual(response.json.get('title'),"Test Section Update Put")
        self.assertEqual(response.json.get('description'),"Test Section Description Put")

    def test_04_section_delete(self):
        response = self.client.delete(f'/section/{self.test_section.id}/delete/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.delete(f'/section/{self.test_section.id}/delete/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_05_section_list(self):
        response = self.client.get(f'/section/')
        self.assertEqual(response.json()['results'][0]['title'],"Test Section Description Put")

    def test_06_section_create_forbidden(self):
        member = get_member_user()
        response = self.client.post(f'/users/token/',{"email":self.user.email, 'password':'qwerty'})
        self.access_token = response.json().get('access'),
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")

        data = {
            'title': "Test Section Create",
            "description": "Test Description Create"

        }
        response = self.client.post('/section/create/',data=data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.json().get('detail'), "У вас недостаточно прав для выполнения даного действия")


