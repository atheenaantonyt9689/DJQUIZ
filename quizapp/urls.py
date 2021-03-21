from django.urls import path 
from .views import HomePageView,QuizDetailView,question_detailView,SignUpView

urlpatterns = [
    path('signup/',SignUpView.as_view(),name='signup'),
    path('post/int:pk>/questions1',question_detailView.as_view,name='questions'),
    path('post/int:pk>/questions',question_detailView.as_view,name='questions'),
    path('post/<int:pk>/',QuizDetailView.as_view(),name ='questions'),
    path('', HomePageView.as_view(),name='home'),

    
]