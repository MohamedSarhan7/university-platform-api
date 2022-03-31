import rest_framework
from django.conf import settings
from django.shortcuts import render
from .models import Department, Student, Doctor, Lecture, Assistant, Subject, Lab
from users.models import NewUser
from users.serializers import NewUserSerializer
# from .serializers import StudentSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .serializers import MyTokenObtainPairSerializer, StudentSerializer, DepartmentSerializer
from .serializers import DoctorSerializer, LectureSerializer, LabSerializer
from .serializers import AssistantSerializer
# from backend.settings import api_settings

# Create your views here.
# from .serializers import MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
# from rest_framework_simplejwt import authentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from django.http import HttpResponse

# from drf_yasg.utils import swagger_auto_schema


def test(request):
    return HttpResponse("working")
# to change claim obtain token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class StudentApi(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        # id=self.request.query_params.get('id')
        user = self.request.user
        # get student return id ,department
        user__ = Student.objects.get(user=user)
        dep = user__.department
        # get_dep=Department.objects.get(pk=dep.pk)
        subjects = dep.subject.all()
        print(subjects)
        print(dep)
        serializer = StudentSerializer(user__)
        return Response(serializer.data)


class StudentDetailApi(APIView):
    # serializer_class = DepartmentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated, )
    # serializer_class = DepartmentSerializer

    def get(self, request):
        user = self.request.user
        student = Student.objects.get(user=user)
        dep = student.department
        serializer = DepartmentSerializer(dep)

        return Response(serializer.data)


def get_subject(name):
    try:
        return Subject.objects.get(name=name)
    except Subject.DoesNotExist:
        raise Http404


class DoctorDetailApi(APIView):
    serializer_class = DoctorSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated, )
    # serializer_class = rest_framework.serializers.Serializer
    detail = "this Subject isn't yours "

    context = {'detail': detail}

    def get_doctor(self):
        doctor = Doctor.objects.get(user=self.request.user)
        return doctor

    def get_Lecture(self, pk):
        try:
            return Lecture.objects.get(pk=pk)
        except Lecture.DoesNotExist:
            raise Http404
    # get doctor subjects and it's lecture

    def get(self, request):
        user = self.request.user
        doctor = Doctor.objects.get(user=user)
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)
    # post new lecture

    # @swagger_auto_schema(request_body=LectureSerializer)
    def post(self, request):

        serializer = LectureSerializer(data=request.data)
        if serializer.is_valid():
            subject = get_subject(serializer.validated_data['subject'])
            doctor = self.get_doctor()
            if doctor == subject.doctor:
                serializer.save()
                return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED)
            else:
                return Response(self.context
                                )
        return Response(
            serializer.data,
            status=status.HTTP_400_BAD_REQUEST)

    # put lecture
    # @swagger_auto_schema(request_body=LectureSerializer)
    def put(self, request):
        pk = self.request.query_params.get('pk')
        lecture = self.get_Lecture(pk=pk)
        doctor = self.get_doctor()

        detail = "this lecture isn't yours "
        cotext = {'msg': detail}
        serializer = LectureSerializer(lecture, data=self.request.data)
        if serializer.is_valid():
            subject = get_subject(serializer.validated_data['subject'])
            if subject == lecture.subject and doctor == subject.doctor:

                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

            else:

                return Response(cotext)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # @swagger_auto_schema(request_body=LectureSerializer)
    def delete(self, request):
        pk = self.request.query_params.get('pk')
        lecture = self.get_Lecture(pk=pk)
        doctor = self.get_doctor()

        # print(doctor.doctor_subjects.all())
        if lecture.subject in doctor.doctor_subjects.all():
            lecture.delete()
            detail = 'deleted'

            context = {
                'msg': detail
            }
            return Response(context)
        else:
            detail = "this Subject isn't yours "
            context = {
                'msg': detail
            }
            return Response(context)


class AssisstantDetailApi(APIView):
    serializer_class = AssistantSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated, )

    def get_assistant(self):
        assistant = Assistant.objects.get(user=self.request.user)
        return assistant

    def get_lab(self, pk):
        try:

            return Lab.objects.get(pk=pk)
        except Lab.DoesNotExist:
            raise Http404

    def get(self, request):
        user = self.request.user

        assistant = Assistant.objects.get(user=user)

        serializer = AssistantSerializer(assistant)
        return Response(serializer.data)

    def post(self, request):
        serializer = LabSerializer(data=request.data)

        if serializer.is_valid():
            subject = get_subject(serializer.validated_data['subject'])
            assistant = self.get_assistant()

            if assistant == subject.assistant:
                serializer.save()

                return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED)
            else:
                context = {
                    'msg': "this subject isn't yours"
                }
                return Response(
                    context

                )
        else:

            return Response(
                serializer.data,
                status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        pk = self.request.query_params.get('pk')

        lab = self.get_lab(pk)

        assistant = self.get_assistant()

        serializer = LabSerializer(lab, data=self.request.data)
        # if assisstant == lab.assisstant:
        if serializer.is_valid():

            subject = get_subject(serializer.validated_data['subject'])
            if subject == lab.subject and assistant == subject.assistant:
                serializer.save()
                detail = 'Updated'
                context = {
                    'msg': detail
                }
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            else:
                detail = 'nothing'
                context = {
                    'msg': detail
                }
                return Response(context)
        else:
            detail = "this lab isn't yours "
            # context = {
            #     'msg': detail
            # }
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        pk = self.request.query_params.get('pk')
        lab = self.get_lab(pk)
        assistant = self.get_assistant()

        # print(doctor.doctor_subjects.all())
        if lab.subject in assistant.assistant_subjects.all():
            lab.delete()
            detail = 'deleted'

            context = {
                'msg': detail
            }
            return Response(context)
        else:
            detail = "this Subject isn't yours "
            context = {
                'msg': detail
            }
            return Response(context)

# class User_pk(APIView):
#     authenticated_classes=(JWTAuthentication)
#     permission_classes=(IsAuthenticated,)
#     def get(self,request):
#         email=request.user

#         user=NewUser.objects.filter(email=email).first()
#         serializer=NewUserSerializer(user)
#         return Response(serializer.data)
