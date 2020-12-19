from django.contrib import admin
from quizApp.models import QuizSet,Question,quizTaker,Response
admin.site.register(QuizSet)
admin.site.register(Question)
admin.site.register(quizTaker)
admin.site.register(Response)