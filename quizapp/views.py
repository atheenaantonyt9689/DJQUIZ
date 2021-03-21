#from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView
from .models import Quiz,Question,Choice
from .forms import CustomUserCreationForm
class HomePageView(ListView):
    model = Quiz
    template_name = 'quiz/home.html'

class QuizDetailView(DetailView):
    model = Quiz
    template_name= 'quiz/questions.html'

class question_detailView(DetailView):
    model = Question
    template_name = 'quiz/questions.html'
class choice(DetailView):
    model = Choice
    template_name = 'quiz/questions.html'

class SignUpView(CreateView):

    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'quiz/signup.html'
