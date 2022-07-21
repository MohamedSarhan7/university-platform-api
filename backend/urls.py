"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from dj_rest_auth.views import PasswordResetView,PasswordResetConfirmView,PasswordChangeView

from django.http import HttpResponse

def empty_view(request):
    return HttpResponse('')


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('api.urls')),
    path("users/",include('users.urls')),
    path("posts/",include("post.urls")),
    path("quiz/",include("quiz.urls")),
    path("api-auth/",include('dj_rest_auth.urls')),
    # path("password/reset",PasswordResetView.as_view()),
    # path("password_reset_confirm/<uid>/<token>",PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
