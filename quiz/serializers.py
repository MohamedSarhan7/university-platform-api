from rest_framework import serializers
from .models import Quizzes, Question, Answer,Grade
from api.models import Subject
from drf_writable_nested import WritableNestedModelSerializer


class AnswerSerializers(serializers.ModelSerializer):
    class Meta:
        model=Answer
        fields=['answer_text','is_right',]  
        
class QuestionSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
    
    answer=AnswerSerializers(many=True)
    
    class Meta:
        model=Question
        fields=['title','answer',]        
        

         
class QuizSerializer(serializers.ModelSerializer):
    question=QuestionSerializer(many=True)
    num_of_question=serializers.IntegerField(source='question.count',read_only=True)
    class Meta:
        model=Quizzes
        fields=['pk','title','subject','num_of_question','question',]
        

class SubjectQuizSerializer(serializers.ModelSerializer):
    subject_quiz=QuizSerializer(many=True)
    class Meta:
        model=Subject
        fields=['pk','name','subject_quiz',]
        
        
class QuizSerializeradd(serializers.ModelSerializer):
    
    class Meta:
        model=Quizzes
        fields=['title','subject',]      
        
class QuestionSerializeradd(serializers.ModelSerializer):
    
    class Meta:
        model=Question
        fields=['title','quiz',]           


class GradeSerializer(serializers.ModelSerializer):
    # quiz=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Grade
        fields=['student','quiz','grade']

# class QuizGradeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Quizzes
#         fields=['pk','title','quiz_grade']

# class QuizSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Quizzes
#         fields = [
#             'title',
#         ]

# class AnswerSerializer(serializers.ModelSerializer):

#     class Meta:
        
#         model = Answer
#         fields = [
#             'id',
#             'answer_text',
#             'is_right',
#         ]

# class RandomQuestionSerializer(serializers.ModelSerializer):

#     answer = AnswerSerializer(many=True, read_only=True)

#     class Meta:
    
#         model = Question
#         fields = [
#             'title','answer',
#         ]


# class QuestionSerializer(serializers.ModelSerializer):

#     answer = AnswerSerializer(many=True, read_only=True)
#     quiz = QuizSerializer(read_only=True)

#     class Meta:
    
#         model = Question
#         fields = [
#             'quiz','title','answer',
        # ]