#from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView,DetailView
from .models import Quiz
class HomePageView(ListView):
    model = Quiz
    template_name = 'quiz/home.html'

class QuizDetailView(DetailView):
    model = Quiz
    template_name= 'quiz/science.html'

class Question(DetailView)