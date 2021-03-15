from django.urls import path
from .views import HomePageView,QuizDetailView

urlpatterns = [
    path('post/<int:pk>/',QuizDetailView.as_view(),name ='science'),
    path('', HomePageView.as_view(),name='home'),

    
]