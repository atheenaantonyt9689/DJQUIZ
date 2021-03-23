# from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from .models import Quiz, Question, Answer
from .forms import CustomUserCreationForm


class HomePageView(ListView):
    model = Quiz
    template_name = "quiz/home.html"


class QuizDetailView(DetailView):
    model = Quiz
    template_name = "quiz/quiz_detail.html"


class QuestionDetailView(DetailView):
    model = Question
    template_name = "quiz/question_detail.html"


class AnswerCreateView(View):
    def post(self, request, *args, **kwargs):

        print("CURRENT User", request.user.id)

        selected_choice = request.POST.get("answer_choice")
        current_user_id = request.user.id
        question_id = request.POST.get("question_id")
        quiz_id = request.POST.get("quiz_id")

        print("Post", selected_choice, ", ")

        # TODO Create and save answer
        answer = Answer(
            user_id=current_user_id,
            selected_choice_id=selected_choice,
            question_id=question_id,
        )
        answer.save()

        return redirect(
            "question_detail",
            quiz_id=quiz_id,
            pk=question_id
        )


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "quiz/signup.html"


# start quiz
class StartQuiz(DetailView):
    model = Quiz
    template_name = "quiz/quiz_start.html"


# detailed view - Questions
# class Questiondetailview(DetailView):
#   model = Question
#  template_name = 'quiz/quiz_start.html'

# class ChoiceQ(DetailView):
#  model = Choice
# template_name = 'quiz/quiz_start.html
