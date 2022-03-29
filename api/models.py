from django.dispatch import receiver
from django.db.models.signals import post_save
from users.models import NewUser
from django.db import models

from django.conf import settings
# Create your models here.


# class Matiral_Lec(models.Model):
#     material_lec = models.FileField(upload_to="uploads/material/lecture")


# class Matiral_Lab(models.Model):
#     material_lab = models.FileField(upload_to="uploads/material/section")


class Doctor(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Assisstant(models.Model):
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
    assisstant = models.ForeignKey(
        Assisstant, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Lecture(models.Model):
    name = models.CharField(max_length=100)
    subject = models.ForeignKey(
        Subject, default='', related_name='subject_lecture', on_delete=models.CASCADE)
    doctor = models.ForeignKey(
        Doctor, default='', related_name='doctor_lec',  on_delete=models.CASCADE)
    material_lec = models.FileField(default='',
                                    upload_to="uploads/material/lecture")

    def __str__(self):
        return self.name


class Lab(models.Model):
    name = models.CharField(max_length=100)
    assisstant = models.ForeignKey(
        Assisstant, null=True, related_name='assisstant_lab', on_delete=models.CASCADE)
    subject = models.ForeignKey(
        Subject, related_name='subject_lab',  null=True, on_delete=models.CASCADE)
    material_lab = models.FileField(
        blank=True, null=True, upload_to="uploads/material/section")

    def __str__(self):
        return self.name


class Result(models.Model):
    subject = models.OneToOneField(Subject, on_delete=models.CASCADE)
    lab_degree = models.DecimalField(
        decimal_places=4, max_digits=4, blank=True, null=True)
    lec_degree = models.DecimalField(
        decimal_places=4, max_digits=4, blank=True, null=True)


class Year(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=100)
    subject = models.ManyToManyField(Subject, related_name='dep_subject')
    year = models.ForeignKey(
        Year, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_subjects(self):
        return self.subject


class Student(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    department = models.ForeignKey(
        Department, blank=True, null=True, on_delete=models.CASCADE)
    # subjects = models.CharField(max_length=200,null=True)
    # result = models.ForeignKey(
    #     Result, blank=True, null=True, on_delete=models.CASCADE)

    # def get_subject(self, *args, **kwargs):
    #     return self.department.subject

    # def save(self, *args, **kwargs):
    #     if self.department:
    #         print(self.department.subjects)
    #         if not self.subjects:
    #             self.subjects = self.get_subject()
    #             super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=NewUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == "1":
            student = Student(user=instance)
            student.save()
        elif instance.user_type == "2":
            doctor = Doctor(user=instance)
            doctor.save()
        elif instance.user_type == "3":
            assisstant = Assisstant(user=instance)
            assisstant.save()
