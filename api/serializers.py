from rest_framework import serializers
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import Department, Student, Doctor, Subject, Lecture
from users.models import NewUser

# to change claim obtain token






class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student

        fields = '__all__'


class LectureSerializer(serializers.ModelSerializer):
    # subject = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Lecture
        fields = ['pk', 'name',  'subject', 'material_lec', ]

    def to_representation(self, instance):
        self.fields['subject'] = serializers.StringRelatedField(read_only=True)
        return super(LectureSerializer, self).to_representation(instance)


class SubjectSerializer(serializers.ModelSerializer):
    doctor = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Subject
        fields = ['pk', 'name', 'doctor', 
                  'full_dgree', 'pass_degree']
        

class DepartmentSerializer(serializers.ModelSerializer):

    subject = SubjectSerializer(many=True)

    class Meta:
        model = Department
        fields = ['dep_name', 'level', 'subject', ]



class DoctorSerializer(serializers.ModelSerializer):
    doctor_subjects = SubjectSerializer(many=True)
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Doctor
        fields = ['pk', 'user', 'doctor_subjects']
