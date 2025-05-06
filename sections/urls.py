from django.urls import path
from rest_framework.routers import DefaultRouter
from os import path as p
from sections.apps import SectionsConfig
from sections.models import Section, Content

from sections.views import SectionListApiView, SectionDestroyAPIView, SectionCreateAPIView, SectionUpdateAPIView, \
    SectionRetrieveApiView, ContentCreateApiView, ContentUpdateAPIView, ContentRetrieveApiView, ContentDestroyAPiView, ContentListApiView

app_name = SectionsConfig.name

router = DefaultRouter()


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
                  path(p.join(section, update), SectionUpdateAPIView.as_view(), name='section_update'),
                  path(p.join(section, delete), SectionDestroyAPIView.as_view(), name='section_delete'),

                  #Content urlpatterns
                  path(p.join(content), ContentListApiView.as_view(), name='content_list'),
                  path(p.join(content, create), ContentCreateApiView.as_view(), name='content_create'),
                  path(p.join(content, update), ContentUpdateAPIView.as_view(), name='content_update'),
                  path(p.join(content, int_pk), ContentRetrieveApiView.as_view(), name='content_detail'),
                  path(p.join(content, delete), ContentDestroyAPiView.as_view(), name='content_delete')

              ] + router.urls
