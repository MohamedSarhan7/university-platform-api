from rest_framework import generics
from rest_framework.response import Response
from .models import Quizzes, Question,Grade
from .serializers import SubjectQuizSerializer,GradeSerializer,QuizSerializeradd,QuestionSerializer,QuestionSerializeradd
# from .serializers import QuizGradeSerializer
from rest_framework.views import APIView
from api.models import Subject,Student,Doctor





class QuizApi(APIView):
    def vaild_student(self,user,subject):
        stu =Student.objects.get(user=user)
        
        if stu.department:
            dep=stu.department
       
            if subject in dep.subject.all():
                return True
            return False
    def vaild_doctor(self,user,subject)  :
          doc=Doctor.objects.get(user=user)
          if subject.doctor == doc:
              return True
          return False
        
        
    def get(self,request):
        user=self.request.user
       
        subjectPK= (request.query_params.get('pk'))
        subject=Subject.objects.get(pk=subjectPK)
        if self.vaild_student(user=user,subject=subject):
            serializer=SubjectQuizSerializer(subject)
            return Response({
                    "status":True,
                    "msg":"succsess",
                    "data":serializer.data
                })
            
        return Response({
                    "status":False,
                    "msg":"not fount or user error",
                   
                })  
    
    
    def post(self,request):
        
        user=self.request.user
       
        subjectPK= (request.query_params.get('pk'))
        subject=Subject.objects.get(pk=subjectPK)
        
        serializer=QuizSerializeradd(data=request.data)
        if serializer.is_valid():
            if self.vaild_doctor(user,subject):
            
                serializer.save()
                return Response( {
                'status':True,
                'msg':"success",
                'data': serializer.data,
                    })
        return Response({
                                 'status':False,
                                 'msg':"err",
                                 'data': serializer.data,
                                 }
                                )
        
        
def valid_QAnswer(answer):
    x=0
    for i in answer:
        if i['is_right']==True:      
               x+=1
    if x!=1:           
        return False 
    return True       
        
class QuestionApi(APIView):
    def post(self,request):
        quizpk= request.query_params.get('pk')
        quiz=Quizzes.objects.get(pk=quizpk)
        serializer=QuestionSerializer(data=request.data)
        if serializer.is_valid():
            answer= serializer.validated_data['answer']
            if valid_QAnswer(answer=answer)!=False:
                serializer.save(quiz=quiz)
                return Response( {
                    'status':True,
                    'msg':"success",
                    'data': serializer.data,
                        })
            return Response({
                                 'status':False,
                                 'msg':"only 1 correct answer !!",
                                 'data': serializer.errors,
                                 }
                                )    
        return Response({
                                 'status':False,
                                 'msg':"err",
                                 'data': serializer.errors,
                                 }
                                )
             
             
             
class QuizGradeApi(APIView):
    def get_student(self,user):
        try:
          return  Student.objects.get(user=user)
        except Student.DoesNotExist:
            return False
    def get(self,request):
       
            
        student=self.get_student(user=self.request.user)
        if student!=False:
            
            grade=Grade.objects.filter(student=student)
            serializer=GradeSerializer(grade,many=True)
            return Response( {
                    'status':True,
                    'msg':"success",
                    'data': serializer.data,
                        })
        
        return  Response( {
                    'status':False,
                    'msg':"user must be student",
                    'data': serializer.data,
                        }) 
    
    def post(self , request):
       serializer=GradeSerializer(data=request.data)
       if self.get_student(user=self.request.user)!=False:
           
            if serializer.is_valid():
               serializer.save(student=self.get_student(self.request.user))
               return Response( {
                    'status':True,
                    'msg':"success",
                    'data': serializer.data,
                        })
        
            return  Response( {
                    'status':False,
                    'msg':"err",
                    'data': serializer.errors,
                        }) 