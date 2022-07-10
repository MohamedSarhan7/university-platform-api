from rest_framework import serializers
from.models import *


        
class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    created_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    class Meta:
        model=Comment
  
        exclude=['post']

class PostSerializerGet(serializers.ModelSerializer):
    post_comments = CommentSerializer(many=True)
    user = serializers.StringRelatedField(read_only=True)
    created_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    class Meta:
        model=Post
        fields=('id',"user","body","image","created_at","post_comments",)
                
                
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=('id',"user","body","image","created_at",)                
    def to_representation(self, instance):
        self.fields['user'] = serializers.StringRelatedField(read_only=True)
        return super(PostSerializer, self).to_representation(instance)    
    
  
        