from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializer import *
from users.models import NewUser
from django.http import Http404

class PostApi(APIView):
    def get_user(name):
        try:
            userx=NewUser.objects.get(name=name)
            return userx
        except NewUser.DoesNotExist:
            raise Http404
                
    def get(self,request):
        posts=Post.objects.all()
        serializer=PostSerializerGet(posts,many=True)
        
        return Response(serializer.data)
    
    def post(self,request):
        
        serializer=PostSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=self.request.user)  
            return Response({
                    "status":True,
                    "msg":"succsess",
                    "data":serializer.data
                })
        return Response({
                    "status":False,
                    "msg":"user error",
                    "data":serializer.data
                })    
   
    
    def get_post(self,pk):
        try:
           return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404    
    def put(self,request):
        post = self.get_post(self.request.query_params.get('pk'))
        
        serializer=PostSerializer(post,data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=self.request.user)  
            return Response({
                    "status":True,
                    "msg":"succsess",
                    "data":serializer.data
                })
        return Response({
                    "status":False,
                    "msg":"user error",
                    "data":serializer.data
                })    
        
        
    def delete(self,request):
        post = self.get_post(self.request.query_params.get('pk'))
       
        if request.user==post.user:
            post.delete()
            return Response({
                    "status":True,
                    "msg":"Deleted",
                   
                })
        return Response({
                    "status":False,
                    "msg":" err",
                   
                })
            
class CommentApi(APIView):
    def get_post(self,pk):
        try:
           return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404
    def post(self,request):
        post=self.get_post(self.request.query_params.get('pk'))
        serializer=CommentSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=self.request.user,post=post)  
            return Response({
                    "status":True,
                    "msg":"succsess",
                    "data":serializer.data
                })
        return Response({
                    "status":False,
                    "msg":"error",
                    "data":serializer.data
                })      
    def get_comment(self,pk):
        try:
            return Comment.objects.get(pk=pk)  
        except Comment.DoesNotExist:
            raise Http404   
    def delete(self,request):
        comment=self.get_comment(self.request.query_params.get('pk'))
        if request.user==comment.user:
            comment.delete()
            return Response({
                    "status":True,
                    "msg":"Deleted",
                   
                })
        return Response({
                    "status":False,
                    "msg":" err",
                   
                })          