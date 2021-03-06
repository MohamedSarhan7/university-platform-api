from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

from django.utils import timezone
# Create your models here.


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, username,user_type, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
      

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, username,user_type, password,  **other_fields)

    def create_user(self, email, username,user_type, password, **other_fields):

        if not email:
            raise ValueError('You must provide an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username
                          ,user_type=user_type, **other_fields)
        user.set_password(password)
        user.save()
        return user


class NewUser(AbstractBaseUser, PermissionsMixin):

    USER_GENDER_CHOICES = (
        ("male", 'male'),
        ("female", 'female'),)

    USER_TYPE_CHOICES = (
        ("student", 'student'),
        ("doctor", 'doctor'),
        ("admin",'admin'))
    email = models.EmailField('email address', unique=True)
    username = models.CharField(max_length=150, unique=True)
    fullname = models.CharField(max_length=150, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    about = models.TextField('about', max_length=500, blank=True)
    gender = models.CharField(
        choices=USER_GENDER_CHOICES, null=True,blank=True, max_length=20)
    date_of_birth = models.DateField(null=True, blank=True)
    user_type = models.CharField(
        choices=USER_TYPE_CHOICES, null=True, max_length=20)
    image=models.ImageField(default='./images/users/default.jpg',upload_to='Profile-Pic/',null=True,blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','fullname','user_type',]

    def __str__(self):
        return self.username
