from django.urls import path
from .views import *

urlpatterns = [
    path("",PostApi.as_view()),
    path("comment",CommentApi.as_view()),
]
