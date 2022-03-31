from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import Department, Student, Doctor, Subject, Lecture, Lab, Assistant
from users.models import NewUser

# to change claim obtain token


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        token['user_type'] = user.user_type
        token['first_name'] = user.first_name
        token['about'] = user.about
        token['gender'] = user.gender
        token['date_of_birth'] = user.date_of_birth

        # ...

        return token


# class NewUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=NewUser
# #         fields='__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student

        fields = '__all__'


class LectureSerializer(serializers.ModelSerializer):
    # doctor = serializers.StringRelatedField(read_only=True)
    # doctor = serializers.PrimaryKeyRelatedField(read_only=True)
    # subject = serializers.StringRelatedField(read_only=True)
    # subject = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Lecture
        fields = ['pk', 'name',  'subject', 'material_lec', ]

    def to_representation(self, instance):
        self.fields['subject'] = serializers.StringRelatedField(read_only=True)
        self.fields['doctor'] = serializers.StringRelatedField(read_only=True)
        return super(LectureSerializer, self).to_representation(instance)


class LabSerializer(serializers.ModelSerializer):
    # assisstant = serializers.StringRelatedField(read_only=True)
    # subject = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Lab
        fields = ['pk', 'name',  'subject', 'material_lab', ]

    def to_representation(self, instance):
        self.fields['subject'] = serializers.StringRelatedField(read_only=True)
        self.fields['assistant'] = serializers.StringRelatedField(
            read_only=True)
        return super(LabSerializer, self).to_representation(instance)


class SubjectSerializer4Assistant(serializers.ModelSerializer):
    doctor = serializers.StringRelatedField(read_only=True)
    assistant = serializers.StringRelatedField(read_only=True)
    subject_lab = LabSerializer(many=True)

    class Meta:
        model = Subject
        fields = ['pk', 'name', 'doctor', 'assistant',
                  'full_dgree', 'pass_degree', 'subject_lab']
class AssistantSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    assistant_subjects =SubjectSerializer4Assistant(many=True)

    class Meta:
        model = Assistant
        fields = ['pk', 'user', 'assistant_subjects']


class SubjectSerializer(serializers.ModelSerializer):
    doctor = serializers.StringRelatedField(read_only=True)
    assistant = serializers.StringRelatedField(read_only=True)
    subject_lecture = LectureSerializer(many=True)
    subject_lab = LabSerializer(many=True)

    class Meta:
        model = Subject
        fields = ['pk', 'name', 'doctor', 'assistant',
                  'full_dgree', 'pass_degree', 'subject_lecture', 'subject_lab']


class DepartmentSerializer(serializers.ModelSerializer):

    subject = SubjectSerializer(many=True)

    class Meta:
        model = Department
        fields = ['name', 'year', 'subject', ]


class SubjectSerializer4Doctor(serializers.ModelSerializer):
    doctor = serializers.StringRelatedField(read_only=True)
    assistant = serializers.StringRelatedField(read_only=True)
    subject_lecture = LectureSerializer(many=True)

    class Meta:
        model = Subject
        fields = ['pk', 'name', 'doctor', 'assistant',
                  'full_dgree', 'pass_degree', 'subject_lecture']


class DoctorSerializer(serializers.ModelSerializer):
    doctor_subjects = SubjectSerializer4Doctor(many=True)
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Doctor
        fields = ['pk', 'user', 'doctor_subjects']
