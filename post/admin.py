from django.contrib import admin
from .models import *
# Register your models here.


class post_admin(admin.ModelAdmin):
    # model = Post
    list_display = ('id', 'user', 'body','created_at')
    list_filter = ('user',)
    # search_fields = ['user__user_name', 'id', 'body',]
admin.site.register(Post,post_admin)
admin.site.register(Comment)