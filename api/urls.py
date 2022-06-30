from .views import test
from django.urls import path,include
from .views import  StudentDetailApi, DoctorDetailApi
# from.views import AssisstantDetailApi

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )



urlpatterns = [
    path("", test),
   
    path('api/student',StudentDetailApi.as_view()),
    path('api/doctor', DoctorDetailApi.as_view()),
    
 
]
