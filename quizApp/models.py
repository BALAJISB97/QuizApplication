from django.db import models
from django.conf import settings

class QuizSet(models.Model):
    quizSetId = models.AutoField(primary_key=True)
    quizName = models.CharField(max_length=20)
    quizAddedTime = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.quizName
    
class Question(models.Model):
    
    quizQuestionId = models.AutoField(primary_key=True)
    quizSetId = models.ForeignKey(QuizSet,on_delete=models.CASCADE)
    quizQuestion = models.TextField()
    option1 = models.CharField(max_length=30)
    option2 = models.CharField(max_length=30)
    option3 = models.CharField(max_length=30)
    option4 = models.CharField(max_length=30)
    answer = models.IntegerField()

class Response(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    quizQuestionId = models.ForeignKey(Question,on_delete=models.CASCADE)
    SelectedOption = models.IntegerField(default=0)
    quizTakerId = models.ForeignKey('quizTaker',on_delete=models.CASCADE)


class quizTaker(models.Model):
    quizTakerId = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    quizSetAttempted = models.ForeignKey(QuizSet,on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    isPassed = models.BooleanField(default=False)
    isCompleted = models.BooleanField(default=False)
    totaltime = models.IntegerField(default=0)
    AttemptedTime = models.DateTimeField(auto_now_add=True)
    
    
    
    
