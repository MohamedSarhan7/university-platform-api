
from django.urls import path, include,re_path
from .views import CustomAuthToken,UserDetailApi



            
urlpatterns = [
    path('', UserDetailApi.as_view()),
    path('token', CustomAuthToken.as_view()),
  
 
]
