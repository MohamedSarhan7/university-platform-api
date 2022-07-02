from rest_framework import serializers
from.models import NewUser

from django.conf import settings
class UserSerializer(serializers.ModelSerializer):
    class Meta:
      
        model=NewUser
        exclude=['id','email','password','last_login','start_date',
                 'user_type','is_superuser','is_staff','is_active','groups','user_permissions']
   
