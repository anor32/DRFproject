from rest_framework.test import APITestCase

from sections.models import Section, Content, Question
from sections.tests.utils import get_admin_user, get_member_user
from rest_framework import status

from sections.urls import section


class QuestionTestCase(APITestCase):

    def setUp(self):
        self.user = get_admin_user()
        response = self.client.post('/users/token/', {"email": self.user.email, 'password': 'qwerty'})
        self.access_token = response.json.get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")
        self.test_section = Section.objects.create(
            title="Test Question",
            description="Test Description",
        )
        self.test_content = Content.otbjects.create(
            section=section.test_section,
            title='Test Title',
            content="Test Content",
        )

        self.test_question = Question.objects.create(
            question_section= self.test_section,
            description='Test question Description',
            question="Test Question",
            answer = "Test Answer"
        )

    def test_13_question_list(self):
        response =self.client.get('/question/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['results'][0]['question'], "Test Question", )


    def test_14_question_is_correct(self):
        response = self.client.get(f'/question/{self.test_question.id}/',)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['question'],'Test Question')

        response = self.client.get(f'/question/{self.test_question.id - 1}/', {"user_answer": "Test Answer"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('is_correct'), True, )

