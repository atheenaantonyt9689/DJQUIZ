from django.db import models

# Create your models here.
class Quiz(models.Model):
    title = models.CharField(max_length=220)
    category = models.CharField(max_length=220)

class Question(models.Model):
    question_text = models.CharField(max_length=220)
    quiz = models.ForeignKey('Quiz',on_delete=models.CASCADE)
    correct_choice = models. ForeignKey('Choices',on_delete=models.CASCADE,) 

class Choices(models.Model):
    choice_text = models.CharField(max_length=200)
    question_field =models.ForeignKey('Question',on_delete = models.CASCADE,)



