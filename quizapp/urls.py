from django.urls import path
from .views import (
    HomePageView,
    AnswerCreateView,
    QuizDetailView,
    AltQuizDetailView,
    QuestionDetailView,
    FinishQuizView,
    SignUpView,
    StartQuiz,
)

urlpatterns = [
    path("choices/int:pk>/questions1", StartQuiz.as_view(), name="quiz_start"),
    path("signup/", SignUpView.as_view(), name="signup"),
    # path('post/int:pk>/questions1',question_detailView.as_view,name='questions'),
    path(
        "quizzes/<int:quiz_id>/questions/<int:pk>/",
        QuestionDetailView.as_view(),
        name="question_detail",
    ),
    path(
        "quizzes/<int:quiz_id>/questions/<int:pk>/answers",
        AnswerCreateView.as_view(),
        name="answer_create",
    ),
    path(
        "quizzes/<int:pk>/finish",
        FinishQuizView.as_view(),
        name="finish_quiz",
    ),
    # path("quizzes/<int:pk>/", QuizDetailView.as_view(), name="quiz_detail"),
    path("quizzes/<int:id>/", AltQuizDetailView.as_view(), name="quiz_detail"),
    path("", HomePageView.as_view(), name="home"),
]
