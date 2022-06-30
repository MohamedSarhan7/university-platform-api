from datetime import date
from django.conf import settings
from django.shortcuts import render
from .models import Department, Student, Doctor, Lecture,  Subject
from users.models import NewUser
from users.serializers import NewUserSerializer
# from .serializers import StudentSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StudentSerializer, DepartmentSerializer
from .serializers import DoctorSerializer, LectureSerializer
# from backend.settings import api_settings

# Create your views here.
# from .serializers import MyTokenObtainPairSerializer
# from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
# from rest_framework_simplejwt import authentication
# from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
# from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from django.http import HttpResponse


def test(request):
    today= date.today()
    return HttpResponse(f"working.. ({today})")



class StudentDetailApi(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        user = self.request.user
        student = Student.objects.get(user=user)
        dep = student.department
        serializer = DepartmentSerializer(dep)

        return Response(serializer.data)





class DoctorDetailApi(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = (IsAuthenticated, )


    def get_doctor(self):
        doctor = Doctor.objects.get(user=self.request.user)
        return doctor
    def get_subject(self,name):
        try:
            return Subject.objects.get(name=name)
        except Subject.DoesNotExist:
            raise Http404
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

    def post(self, request):

        serializer = LectureSerializer(data=request.data)
        if serializer.is_valid():
            subject = self.get_subject(serializer.validated_data['subject'])
           
            doctor = self.get_doctor()
            if doctor ==subject.doctor:
                serializer.save()
                return Response( {
                'status':"true",
                'msg':"success",
                'data': serializer.data,
                    })
            else:
                return Response({
                                 'status':"false",
                                 'msg':"this Subject isn't yours",
                                 'data': serializer.data,
                                 }
                                )
        return Response(
            {
                'status':"false",
                'msg':"data not valid",
                'data': serializer.data,
            }
            )


    # put lecture


    def put(self, request):
        pk = self.request.query_params.get('pk')
        lecture = self.get_Lecture(pk=pk)
        doctor = self.get_doctor()

        serializer = LectureSerializer(lecture, data=self.request.data)
        if serializer.is_valid():
          
            subject = self.get_subject(serializer.validated_data['subject'])
            if subject == lecture.subject  and doctor == subject.doctor:

                serializer.save()
                return Response( {
                'status':"true",
                'msg':"success",
                'data': serializer.data,
                    })

            else:

                return Response({
                                 'status':"false",
                                 'msg':"this Subject isn't yours",
                                 'data': serializer.data,
                                 })

        return Response({
                                 'status':"false",
                                 'msg':"data not valid",
                                 'data': serializer.data,
                                 })

    def delete(self, request):
        pk = self.request.query_params.get('pk')
        lecture = self.get_Lecture(pk=pk)
        doctor = self.get_doctor()

      
        if lecture.subject in doctor.doctor_subjects.all():
            lecture.delete()
           
            return Response({
                'status':'true',
                'msg': 'Deleted'
            })
        else:
           
            return Response({
                'status':"false",
                'msg': "this Subject isn't yours "
            })

