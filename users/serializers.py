from rest_framework import serializers
from.models import NewUser


class NewUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=NewUser
        exclude=['id','password']
        # fields='__all__'
        # fields=['email','username','user_type','student_id','doctor_id',]

