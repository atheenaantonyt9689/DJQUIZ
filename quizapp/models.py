from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse 

# Create your models here.
class Quiz(models.Model):
    title = models.CharField(max_length=220)
    category = models.CharField(max_length=220)
       
    def __str__(self):
        return self.title
    #def get_absolute_url(self): 
       # return reverse('questions', args=[str(self.id)])


class Question(models.Model):

    image = models.CharField(max_length=220) 
    question_text = models.CharField(max_length=220)
    quiz = models.ForeignKey('Quiz',on_delete=models.CASCADE)
    correct_choice = models. ForeignKey('Choice',on_delete=models.CASCADE,blank=True,null=True) 
    
    def __str__(self):
        return self.question_text
    #def get_absolute_url(self): 
        #return reverse('questions', args=[str(self.id)])
    
class Choice(models.Model):
    choice_text = models.TextField()
    question_field =models.ForeignKey('Question',on_delete = models.CASCADE,)
    def __str__(self):
        return self.choice_text

#custom user model
class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(null=True,blank=True)
    def __str__(self):
        return self.first_name


#answer model
class Answer(models.Model):
     user = models.ForeignKey('CustomUser',on_delete=models.CASCADE,)
     question = models.ForeignKey('Question',on_delete = models.CASCADE,)
     selected_choice = models.ForeignKey('Choice',on_delete=models.CASCADE,)

