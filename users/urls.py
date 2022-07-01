
from django.urls import path, include
from .views import CustomAuthToken


urlpatterns = [
   
    path('token', CustomAuthToken.as_view()),
    path("api-auth/",include('dj_rest_auth.urls')),#login pw-rest pw-rest-confirm pw-change
]
