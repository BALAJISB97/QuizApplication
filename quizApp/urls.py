from django.contrib import admin
from django.urls import path,include
from quizApp import views

urlpatterns = [
    path('',views.home,name="home"),
    path('login',views.loginn,name="login"),
    path('signup',views.signup,name="signup"),
    path('logout',views.Logout,name="logout"),
    path('quizset',views.quizset,name="quizset"),
    #id1 => QuizSetId
    path('takequiz/<int:id1>',views.takequiz,name='takequiz'),
    #id1 => QuizSetId | id2 => QuizTakerId
    path('runquiz/<int:id1>/<int:id2>',views.runquiz,name='runquiz'),
    #id1=> QuestionId | id2 => QuizTakerId
    path('saveResponse/<int:id1>/<int:id2>',views.save,name='save'),
    path('endquiz/<int:id1>',views.endquiz,name='endquiz'),
    path('results',views.results,name='endquiz'),
    ]