from django.contrib import admin

# Register your models here.
from users.models import NewUser
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea, CharField
from django import forms
from django.db import models


class UserAdminConfig(UserAdmin):
    model = NewUser
    search_fields = ('email', 'username', 'fullname',)
    list_filter = ('email', 'username', 'fullname', 'is_active', 'is_staff')
    ordering = ('-start_date',)
    list_display = ('email','id', 'username', 'fullname',
                    'is_active', 'is_staff')
    fieldsets = [
        (None, {'fields': ('email', 'username', 'fullname','image', 'about', 'gender', 'date_of_birth',)}),
        ('Permissions', {'fields': ('user_type','is_staff', 'is_active')}),
        
    ]
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'fullname','user_type', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )


admin.site.register(NewUser, UserAdminConfig)
