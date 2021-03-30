# from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from django.contrib import messages  # import messages

from .models import Quiz, Question, Answer
from .forms import CustomUserCreationForm


class HomePageView(ListView):
    model = Quiz
    template_name = "quiz/home.html"


class QuizDetailView(DetailView):
    model = Quiz
    template_name = "quiz/quiz_detail.html"


class FinishQuizView(View):
    def post(self, request, *args, **kwargs):
        # TODO
        quiz_id = kwargs.get("pk")
        quiz = Quiz.objects.get(id=quiz_id)
        template_name = "quiz/finish_quiz.html"
        # question_id_list = [3,5,6,7,10,11]

        # find question list
        # for each question find correct-answer choice_text
        # create dictionary
        correct_answers = {}
        for question in question_set:
            correct_answers[question.id] = "correct choice text"
        """
        correct_answers = {
            3: "Trivandrum",
            5: "Chennai",
            6: "Bangalore",
        }
        """
        # find question list
        # for each question find correct-answer choice_text
        # create dictionary
        selected_answers = {}
        for question in question_set:
            selected_answers[question.id] = "selected choice text"
        """
        selected_answers = {
            3: "Trivandrum",
            5: "Chennai",
            6: "Belgaum",
        }
        """

        context = {"quiz": quiz, "selected_answers": {}, "correct_answers": {}}
        return render(request, template_name, context)


class AltQuizDetailView(View):
    def get(self, request, *args, **kwargs):
        print("args, kwargs", args, kwargs)
        print("request.GET", request.GET)

        quiz_id = kwargs.get("id")
        quiz = Quiz.objects.get(id=quiz_id)

        first_question = Question.objects.filter(quiz_id=quiz_id).order_by("id").first()
        template_name = "quiz/quiz_detail2.html"
        context = {"quiz": quiz, "first_question": first_question}
        return render(request, template_name, context)


class QuestionDetailView(View):
    # model = Question
    # template_name = "quiz/question_detail.html"

    def get(self, request, *args, **kwargs):
        print("args, kwargs", args, kwargs)
        print("request.GET", request.GET)

        quiz_id = kwargs.get("quiz_id")
        question_id = kwargs.get("pk")
        quiz = Quiz.objects.get(id=quiz_id)
        question = Question.objects.get(id=question_id)

        answered_choice = Answer.objects.filter(
            user_id=request.user.id, question_id=question_id
        ).last()
        # previous_question =

        template_name = "quiz/question_detail.html"
        context = {
            "quiz": quiz,
            "question": question,
            "answered_choice": answered_choice,
            "previous": previous_question_id,  # TODO
            "next": next_question_id,  # TODO
            "next_disabled": next_question_disabled,
            "previous_disabled": previous_question_disabled,
        }
        return render(request, template_name, context)


class AnswerCreateView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):

        print("CURRENT User", request.user.id)

        selected_choice = request.POST.get("answer_choice")

        current_user_id = request.user.id
        question_id = request.POST.get("question_id")
        quiz_id = request.POST.get("quiz_id")

        if selected_choice is None:
            messages.warning(request, "Please select atleast one choice!")
            return redirect("question_detail", quiz_id=quiz_id, pk=question_id)

        quiz = Quiz.objects.get(id=quiz_id)
        # question = Question.objects.get(id=question_id)

        print("Selected Choice", selected_choice, ", ")

        # TODO Create and save answer
        answer = Answer(
            user_id=current_user_id,
            selected_choice_id=selected_choice,
            question_id=question_id,
        )
        answer.save()

        questions = [
            question.id
            for question in Question.objects.filter(quiz_id=quiz_id).order_by("id")
        ]

        next_question_id = question_id

        try:
            qindex = questions.index(int(question_id))
            print("qIndex", qindex)
            if qindex == len(questions) - 1:
                last_question = True
                next_question_id = question_id
            else:
                next_index = qindex + 1
                next_question_id = questions[next_index]
        except ValueError:
            print("valueerror")

        print("Next question id", next_question_id)

        return redirect("question_detail", quiz_id=quiz_id, pk=next_question_id)
        # return render()


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
