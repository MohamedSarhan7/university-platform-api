from django.db import models
from django.conf import settings
from users.models import NewUser
# Create your models here.

class Post(models.Model):
    user=models.ForeignKey(NewUser,on_delete=models.CASCADE,blank=True,related_name='user_posts')
    body=models.TextField()
    image=models.ImageField(upload_to='Posts/',null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.body
class Comment(models.Model):
    user=models.ForeignKey(NewUser,on_delete=models.CASCADE)
    body=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='post_comments')
    
    class Meta:
        ordering=("created_at",)
    def __str__(self):
        return self.body
    
# class Like(models.Model):
#     user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
#     post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='post_likes')