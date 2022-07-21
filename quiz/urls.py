from django.urls import path
from .views import QuizApi,QuestionApi,QuizGradeApi

app_name='quiz'

urlpatterns = [
    path('', QuizApi.as_view()),
    path('question', QuestionApi.as_view()),
    path('quiz-grade', QuizGradeApi.as_view()),

]