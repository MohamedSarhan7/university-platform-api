from django.contrib import admin
from .models import Subject, Lab, Assistant, Lecture, Result, Department

from .models import Year, Student, Doctor
# Register your models here.
# x = Department.objects.get(id=7)


# x = Student.objects.all()
# print(x)


class dep_admin(admin.ModelAdmin):
    list_display = ('name', 'year')
    list_filter = ('year',)


class subject_admin(admin.ModelAdmin):
    list_display = ('name', 'pk', 'doctor', 'assistant',)
    list_filter = ('doctor', 'assistant',)


class student_admin(admin.ModelAdmin):
    list_display = ('user', 'department')
    list_filter = ('department',)


class lecture_admin(admin.ModelAdmin):
    list_display = ('subject', 'name', 'pk',)
    list_filter = ('subject',)


class lab_admin(admin.ModelAdmin):
    list_display = ('subject',  'name', 'pk',)
    list_filter = ('subject',)


admin.site.register(Year)
admin.site.register(Department, dep_admin)
admin.site.register(Subject, subject_admin)
admin.site.register(Student, student_admin)
admin.site.register(Doctor)
admin.site.register(Assistant)
admin.site.register(Lab, lab_admin)
admin.site.register(Lecture, lecture_admin)
admin.site.register(Result)
