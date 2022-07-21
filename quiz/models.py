from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
from api.models import Subject,Student
from users.models import NewUser


class Quizzes(models.Model):
    
    class Meta:
        verbose_name = _("Quiz")
        verbose_name_plural = _("Quizzes")
        ordering = ['id']

    title = models.CharField(max_length=255, default=_(
        "New Quiz"), verbose_name=_("Quiz Title"))
    subject = models.ForeignKey(
        Subject,related_name='subject_quiz', default=1, on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Updated(models.Model):
    
    date_updated = models.DateTimeField(
        verbose_name=_("Last Updated"), auto_now=True)

    class Meta:
        abstract = True    
        
        
class Question(Updated):
    
    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")
        ordering = ['id']

   

    quiz = models.ForeignKey(
        Quizzes, related_name='question', on_delete=models.CASCADE)
    
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    
    date_created = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Date Created"))
    is_active = models.BooleanField(
        default=False, verbose_name=_("Active Status"))

    def __str__(self):
        return self.title        
    
    
class Answer(Updated):
    
    class Meta:
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")
        ordering = ['id']

    question = models.ForeignKey(
        Question, related_name='answer', on_delete=models.CASCADE)
    answer_text = models.CharField(
        max_length=255, verbose_name=_("Answer Text"))
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text    
    
    
class Grade(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE,blank=True)
    quiz=models.ForeignKey(Quizzes,on_delete=models.CASCADE)
    grade=models.IntegerField()
    
    def __str__(self):
        return str(self.student)
       