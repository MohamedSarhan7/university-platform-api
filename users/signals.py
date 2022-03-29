# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from api.models import Student, Doctor
# from .models import NewUser


# @receiver(post_save, sender=NewUser)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         if instance.user_type == "1":
#             student = Student(user=instance)
#             student.save()
#         elif instance.user_type == "2":
#             doctor = Doctor(user=instance)
#             doctor.save()


# post_save.connect(create_user_profile, sender=NewUser)
