from django.shortcuts import render
from django.views.generic import DeleteView
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from urllib3 import request

from sections.models import Section, Content, Question
from sections.permissions import IsModerator
from sections.serializers.question_serializers import QuestionSectionSerializer, QuestionSerializer
from sections.serializers.section_serializers import SectionSerializer, SectionListSerializer
from sections.serializers.context_serializers import ContentSerializer, ContentListSerializer, \
    ContentListSerializer

from sections.paginators import SectionPaginator, SectionContentPaginator, QuestionPaginator


class SectionListApiView(ListAPIView):
    serializer_class = SectionListSerializer
    queryset = Section.objects.all()
    # permission_classes = (IsAuthenticated,)
    # permission_clas = SectionPaginator


class SectionCreateAPIView(CreateAPIView):
    serializer_class = SectionSerializer
    # permission_classes = (IsAuthenticated, IsAdminUser | IsModerator)


class SectionRetrieveApiView(RetrieveAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    # permission_classes = (IsAuthenticated,)


class SectionUpdateAPIView(UpdateAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    # permission_classes = (IsAuthenticated, IsAdminUser | IsModerator)


class SectionDestroyAPIView(DestroyAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    # permission_classes = (IsAuthenticated, IsAdminUser | IsModerator)

#content
class ContentListApiView(ListAPIView):
    serializer_class = ContentSerializer
    queryset = Content.objects.all()
    # permission_classes = (IsAuthenticated,)
    pagination_class = SectionContentPaginator


class ContentRetrieveApiView(RetrieveAPIView):
    serializer_class = ContentSerializer
    queryset = Content.objects.all()
    # permission_classes = (IsAuthenticated,)


class ContentCreateApiView(RetrieveAPIView):
    serializer_class = ContentSerializer
    queryset = Content.objects.all()
    # permission_classes = (IsAuthenticated,)


class ContentUpdateAPIView(UpdateAPIView):
    serializer_class =  ContentSerializer
    queryset = Content.objects.all()
    # permission_classes = (IsAuthenticated, IsAdminUser | IsModerator)


class ContentDestroyAPiView(DestroyAPIView):
    serializer_class =  ContentSerializer
    queryset = Content.objects.all()
    # permission_classes = (IsAuthenticated, IsAdminUser | IsModerator)



class QuestionListApiView(ListAPIView):
    serializer_class =  QuestionSerializer
    queryset = Question.objects.all()
    # permission_classes = (IsAuthenticated,)
    pagination_class = QuestionPaginator



class QuestionRetrieveApiView(RetrieveAPIView):
    serializer_class = QuestionSectionSerializer
    queryset = Question.objects.all()

    # permission_classes = (IsAuthenticated,)

    def post(self,request ,*args, **kwargs):
        answers = [question.answer for question in Question.objects.all()]
        answer = answers[self.kwargs.get('pk')-1].strip().lower()
        user_answer = request.data.get('user_answer').strip().lower()
        is_correct = user_answer == answer
        return Response({'is_correct':is_correct})


