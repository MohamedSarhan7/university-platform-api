from django.contrib import admin
from . import models
from .models import Grade
# Register your models here.

class grade_admin(admin.ModelAdmin):
    list_display = ('student', 'quiz', 'grade',)
    list_filter = ('quiz',)
admin.site.register(Grade,grade_admin)


@admin.register(models.Quizzes)

class QuizAdmin(admin.ModelAdmin):
	list_display = [
        'id', 
        'title',
        ]

class AnswerInlineModel(admin.TabularInline):
    model = models.Answer
    fields = [
        'answer_text', 
        'is_right'
        ]

@admin.register(models.Question)

class QuestionAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'quiz',
        ]
    list_display = [
        'title', 
        'quiz',
        'date_updated'
        ]
    inlines = [
        AnswerInlineModel, 
        ] 

@admin.register(models.Answer)

class AnswerAdmin(admin.ModelAdmin):
    list_display = [
        'answer_text', 
        'is_right', 
        'question'
        ]