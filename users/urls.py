
from django.urls import path, include
from .views import Logout_BlacklistTokenUpdateView

urlpatterns = [
   
    path("logout",Logout_BlacklistTokenUpdateView.as_view()),
]
