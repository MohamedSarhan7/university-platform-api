from django.conf import settings
from django.shortcuts import render
from .models import Department, Student, Doctor, Lecture,Assisstant,Subject,Lab
from users.models import NewUser
from users.serializers import NewUserSerializer
# from .serializers import StudentSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MyTokenObtainPairSerializer, StudentSerializer, DepartmentSerializer
from .serializers import DoctorSerializer, LectureSerializer, LabSerializer
from .serializers import AssisstantSerializer
# from backend.settings import api_settings

# Create your views here.
# from .serializers import MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
# from rest_framework_simplejwt import authentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication


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
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        user = self.request.user
        student = Student.objects.get(user=user)
        dep = student.department
        serializer = DepartmentSerializer(dep)

        return Response(serializer.data)


class DoctorDetailApi(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated, )
    
    

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
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED)
        return Response(
            serializer.data,
            status=status.HTTP_400_BAD_REQUEST)
    def get_doctor(self):
        doctor = Doctor.objects.get(user=self.request.user)
        return doctor
    def get_Lecture(self, pk):
        try:
            return Lecture.objects.get(pk=pk)
        except Lecture.DoesNotExist:
            raise Http404
    
           
    # put lecture

    def put(self, request):
        pk = self.request.query_params.get('pk')
        lecture = self.get_Lecture(pk=pk)
        doctor = self.get_doctor()
        detail = ''
        
        if doctor == lecture.doctor:

            serializer = LectureSerializer(lecture, data=self.request.data)
            if serializer.is_valid():
                serializer.save()
                detail = 'Updated'
                # context = {
                #     'msg': detail
                # }
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
                
        else:
                detail = "this lecture isn't yours "
                # context = {
                #     'msg': detail
                # }
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        pk = self.request.query_params.get('pk')
        lecture = self.get_Lecture(pk=pk)
        doctor=self.get_doctor()
      
        detail = ''
        
        if doctor ==lecture.doctor:
      
            lecture.delete()
            detail = 'deleted'
        else:
            detail = "this lecture isn't yours "
        context = {
            'msg': detail
        }
        return Response(context)



class  AssisstantDetailApi(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated, )
    def get_subject(slef,name):
        try:
            return Subject.objects.get(name=name)
        except Subject.DoesNotExist:
            raise Http404
    def get_assisstant(self):
        doctor = Assisstant.objects.get(user=self.request.user)
        return doctor
    def get_lab(self,pk):
        try:
            # print(Lab.objects.get(pk=pk))
            return Lab.objects.get(pk=pk)
        except Lab.DoesNotExist:
            raise Http404
        
   
    def get(self, request):
        user = self.request.user
        
        assisstant = Assisstant.objects.get(user=user)
        print(assisstant)
        serializer = AssisstantSerializer(assisstant)
        return Response(serializer.data)

    def post(self, request):
        serializer = LabSerializer(data=request.data)
        
        if serializer.is_valid():
            subject = self.get_subject(serializer.validated_data['subject'])
            # assisstant = self.get_assisstant()
            assisstant = serializer.validated_data['assisstant']
            if assisstant == subject.assisstant:
                serializer.save()
                
                return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED)
            else:
                context={
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
        
        assisstant = self.get_assisstant()
        detail = ''

        if assisstant == lab.assisstant:

            serializer = LabSerializer(lab, data=self.request.data)
            if serializer.is_valid():
                serializer.save()
                detail = 'Updated'
                # context = {
                #     'msg': detail
                # }
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        else:
            detail = "this lecture isn't yours "
            # context = {
            #     'msg': detail
            # }
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class User_pk(APIView):
#     authenticated_classes=(JWTAuthentication)
#     permission_classes=(IsAuthenticated,)
#     def get(self,request):
#         email=request.user

#         user=NewUser.objects.filter(email=email).first()
#         serializer=NewUserSerializer(user)
#         return Response(serializer.data)
