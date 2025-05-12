from django.contrib import admin

from sections.models import Section, Content, Question


# Register your models here.

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    list_filter = ('title',)
    ordering = ('id',)


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'section','ttile')
    list_filter = ('section',)
    ordering = ('id','section')

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id','question_section','description','answer')
    list_filter = ('question_section',)
    ordering = ('id','question_section')