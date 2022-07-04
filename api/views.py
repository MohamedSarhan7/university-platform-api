from datetime import date
from .models import Department, Student, Doctor, Lecture,  Subject
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StudentSerializer, DepartmentSerializer
from .serializers import DoctorSerializer, LectureSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http.response import JsonResponse  
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

        return Response( {
                'status':True,
                'msg':"success",
                'data': serializer.data,
                    })




class DoctorDetailApi(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = (IsAuthenticated, )


    # get doctor subjects and it's lecture

    def get(self, request):
        user = self.request.user
        doctor = Doctor.objects.get(user=user)
        serializer = DoctorSerializer(doctor)
        return Response( {
                'status':True,
                'msg':"success",
                'data': serializer.data,
                    })
  
  
class LectureApi (APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = (IsAuthenticated, )
    def get_doctor(self):
        doctor = Doctor.objects.get(user=self.request.user)
        return doctor
    def get_subject(self,pk):
        try:
            return Subject.objects.get(pk=pk)
        except Subject.DoesNotExist:
            raise Http404
        
    def get_subject4put(self,name):
        try:
            return Subject.objects.get(name=name)
        except Subject.DoesNotExist:
            raise Http404    
    def get_Lecture(self, pk):
        try:
            return Lecture.objects.get(pk=pk)
        except Lecture.DoesNotExist:
            raise Http404
    
    
    def get(self,request):
        pk = self.request.query_params.get('pk')
        subject = self.get_subject(pk=pk)
        lecture=Lecture.objects.filter(subject=subject)
        serializer=LectureSerializer(lecture,many=True)
        
        return  Response( {
                'status':True,
                'msg':"success",
                'data': serializer.data,
                    })
    def post(self, request):
    
        serializer = LectureSerializer(data=request.data)
        if serializer.is_valid():
            subject = self.get_subject4put(serializer.validated_data['subject'])
           
            doctor = self.get_doctor()
            if doctor ==subject.doctor:
                serializer.save()
                return Response( {
                'status':True,
                'msg':"success",
                'data': serializer.data,
                    })
            else:
                return Response({
                                 'status':False,
                                 'msg':"this Subject isn't yours",
                                 'data': serializer.data,
                                 }
                                )
        return Response(
            {
                'status':False,
                'msg':"data not valid",
                'data': serializer.data,
            }
            )

    
    
    def put(self, request):
        pk = self.request.query_params.get('pk')
        lecture = self.get_Lecture(pk=pk)
        doctor = self.get_doctor()

        serializer = LectureSerializer(lecture, data=self.request.data)
        if serializer.is_valid():
            # print(serializer.validated_data['subject'])
            # return(JsonResponse(serializer.data))
            subjectx = self.get_subject4put(serializer.validated_data['subject'])
            if subjectx == lecture.subject  and doctor == subjectx.doctor:

                serializer.save()
                return Response( {
                'status':True,
                'msg':"success",
                'data': serializer.data,
                    })

            else:

                return Response({
                                 'status':False,
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
                'status':True,
                'msg': 'Deleted'
            })
        else:
           
            return Response({
                'status':False,
                'msg': "this Subject isn't yours "
            })    