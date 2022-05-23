from .views import test
from django.urls import path
from .views import MyTokenObtainPairView, StudentDetailApi, DoctorDetailApi
from.views import AssisstantDetailApi

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



urlpatterns = [
    path("", test),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/student',StudentDetailApi.as_view()),
    path('api/doctor', DoctorDetailApi.as_view()),
    path('api/assisstant', AssisstantDetailApi.as_view()),
 
]
