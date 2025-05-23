from django.urls import path
from rest_framework.routers import DefaultRouter
from os import path as p
from sections.apps import SectionsConfig
from sections.models import Section, Content, Question

from sections.views import SectionListApiView, SectionDestroyAPIView, SectionCreateAPIView, SectionUpdateAPIView, \
    SectionRetrieveApiView, ContentCreateApiView, ContentUpdateAPIView, ContentRetrieveApiView, ContentDestroyAPiView, \
    ContentListApiView, QuestionRetrieveApiView, QuestionListApiView

app_name = SectionsConfig.name

router = DefaultRouter()

questions = 'questions/'
section = 'section/'
create = 'create/'
update = 'update/'
delete = 'delete/'
int_pk = '<int:pk>/'
content = 'content/'
urlpatterns = [
                  # Section urlpatterns
                  path(p.join(section, ), SectionListApiView.as_view(), name='section_list'),
                  path(p.join(section, create), SectionCreateAPIView.as_view(), name='section_create'),
                  path(p.join(section, int_pk), SectionRetrieveApiView.as_view(), name='section_detail'),
                  path(p.join(section, int_pk, update, ), SectionUpdateAPIView.as_view(), name='section_update'),
                  path(p.join(section, int_pk, delete), SectionDestroyAPIView.as_view(), name='section_delete'),

                  # Content urlpatterns
                  path(p.join(content), ContentListApiView.as_view(), name='content_list'),
                  path(p.join(content ,create), ContentCreateApiView.as_view(), name='content_create'),
                  path(p.join(content, int_pk, update), ContentUpdateAPIView.as_view(), name='content_update'),
                  path(p.join(content, int_pk), ContentRetrieveApiView.as_view(), name='content_detail'),
                  path(p.join(content, int_pk, delete), ContentDestroyAPiView.as_view(), name='content_delete'),
                  # question urls
                  path(p.join(questions, ), QuestionListApiView.as_view(), name='question_list'),
                  path(p.join(questions, int_pk), QuestionRetrieveApiView.as_view(), name='question_read'),

              ] + router.urls
