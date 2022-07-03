from django.dispatch import receiver
from django.db.models.signals import post_save
from users.models import NewUser
from django.db import models

from django.conf import settings
import uuid
# Create your models here.




class Doctor(models.Model):
   
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username




class Subject(models.Model):
   
    name = models.CharField(max_length=100)
    full_dgree = models.IntegerField(default=100)
    pass_degree = models.IntegerField(default=50)
    doctor = models.ForeignKey(
        Doctor,  blank=True, null=True, related_name='doctor_subjects', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class Lecture(models.Model):
  
    name = models.CharField(max_length=100)
    subject = models.ForeignKey(
        Subject, default='', related_name='subject_lecture', on_delete=models.CASCADE)
    
    material_lec = models.FileField(
                                    upload_to="material/lecture/")

    def __str__(self):
        return self.name








class Level(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Department(models.Model):
   
    dep_name = models.CharField(max_length=100)
    subject = models.ManyToManyField(Subject, related_name='dep_subject')
    level = models.ForeignKey(
        Level, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.dep_name

    def get_subjects(self):
        return self.subject


class Student(models.Model):
  
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    department = models.ForeignKey(
        Department, blank=True, null=True, on_delete=models.CASCADE)
    
 

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=NewUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == "student":
            student = Student(user=instance)
            student.save()
        elif instance.user_type == "doctor":
            doctor = Doctor(user=instance)
            doctor.save()
       
