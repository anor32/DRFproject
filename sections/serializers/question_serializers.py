from rest_framework.generics import RetrieveAPIView

from sections.models import Question
from rest_framework.serializers import  ModelSerializer
from rest_framework.relations import SlugRelatedField

from sections.models import Question,Section

class QuestionSectionSerializer(ModelSerializer):
    question_section = SlugRelatedField(slug_field='title',queryset=Section.objects.all())

    class Meta:
        model = Question
        fields = ('id','question_section')


class QuestionSerializer(ModelSerializer):
    question_section = SlugRelatedField(slug_field='title',queryset=Section.objects.all())

    class Meta:
        model = Question
        fields = ('id','question_section','question')


class QuestionCreateSerializer(ModelSerializer):
    question_section = SlugRelatedField(slug_field='title', queryset=Section.objects.all())

    class Meta:
        model = Question
        fields = '__all__'

