from django.urls import path 
from .views import HomePageView,QuizDetailView,question_detailView,SignUpView

urlpatterns = [
    #path('choices/int:pk>/questions1',StartQuiz.as_view,name='quiz_start'),
    
    path('signup/',SignUpView.as_view(),name='signup'),
    path('post/int:pk>/questions1',question_detailView.as_view,name='questions'),
    path('post/int:pk>/questions11',question_detailView.as_view,name='questions'),
    path('questions/<int:pk>/question/',QuizDetailView.as_view(),name ='questions'),    
    path('', HomePageView.as_view(),name='home'),

    
]