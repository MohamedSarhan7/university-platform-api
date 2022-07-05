from rest_framework import serializers
from.models import NewUser
from post.serializer import PostSerializerGet

from django.conf import settings
class UserSerializerGet(serializers.ModelSerializer):
    user_posts= PostSerializerGet(many=True)
    class Meta:
        
        model=NewUser
        # exclude=['email','password','last_login','start_date',
                #  'user_type','is_superuser','is_staff','is_active','groups','user_permissions']
   
        fields=('email',"username","fullname",'about','gender',"image",'date_of_birth',"user_posts",)
        
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        
        model=NewUser
        exclude=['email','password','last_login','start_date',
                 'user_type','is_superuser','is_staff','is_active','groups','user_permissions']
   
               