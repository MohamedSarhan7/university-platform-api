from django.contrib import admin
from .models import Subject,  Lecture, Department

from .models import Level, Student, Doctor



class dep_admin(admin.ModelAdmin):
    list_display = ('dep_name', 'level')
    list_filter = ('level',)


class subject_admin(admin.ModelAdmin):
    list_display = ('name', 'pk', 'doctor', )
    list_filter = ('doctor', )


class student_admin(admin.ModelAdmin):
    list_display = ('user', 'department')
    list_filter = ('department',)


class lecture_admin(admin.ModelAdmin):
    list_display = ('subject', 'name', 'pk',)
    list_filter = ('subject',)


admin.site.register(Level)
admin.site.register(Department, dep_admin)
admin.site.register(Subject, subject_admin)
admin.site.register(Student, student_admin)
admin.site.register(Doctor)

admin.site.register(Lecture, lecture_admin)

