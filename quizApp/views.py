from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User,auth,AnonymousUser
from django.contrib import messages
from quizApp.models import QuizSet,Question,Response,quizTaker

def home(request):
    return render(request,'home.html')

def loginn(request):
    if request.method=='POST':
        username,password=request.POST['username'],request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            print('Login done')
            messages.info(request,'Authenticated!')
            return render(request,'home.html')
        else:
            messages.info(request,'invalid credentials')
        
    return render(request,'login.html')

def signup(request):
    if request.method=='POST':
        firstName,lastName,userName,password1,password2,email=request.POST['firstname'],request.POST['lastname'],request.POST['Username'],request.POST['password'],request.POST['password2'],request.POST['email']
        if password1==password2:
            if User.objects.filter(username=userName).exists():
                messages.info(request,'username taken')
            else:
                user = User.objects.create_user(first_name=firstName,last_name=lastName,password=password1,username=userName,email=email)
                user.save()
                redirect('/')
        else:
            messages.info(request,'Password not matching!')
        
    return render(request,'signup.html')


def Logout(request):
    auth.logout(request)
    return render(request,'home.html')

def quizset(request):
    quiz = QuizSet.objects.all()
    quizDict = {'quizset':quiz}
    return render(request,'viewQuizSet.html',quizDict)
        
#id1=> QuizsetId
def takequiz(request,id1):
    if is_logn(request):
        quizSetAttempted = QuizSet.objects.get(pk=id1)
        obj = quizTaker(user=request.user,quizSetAttempted=quizSetAttempted)
        obj.save()
        #QuizTakerId
        id2 = obj.quizTakerId
        return redirect(runquiz,id1,id2)
    else:
        return redirect('/login')

def is_logn(request):
    if request.user!=AnonymousUser():
        return True
    return False

#id1 => QuizSetId | id2 => QuizTakerId
def runquiz(request,id1,id2):
    question = Question.objects.filter(quizSetId=id1)
    quizTakerobj = quizTaker.objects.get(pk=id2)
    context = {'question':question,'quizTaker':quizTakerobj}
    responeObj = Response.objects.filter(quizTakerId=quizTakerobj)
    print(responeObj)
    recordedResponse={}
    for resp in responeObj:
        questionId,selectedOption=resp.quizQuestionId,resp.SelectedOption
        qId=questionId.quizQuestionId
        recordedResponse[qId]=selectedOption
    context['recordedResponse']=recordedResponse
    return render(request,'runquiz.html',context)
    
#id1=> QuestionId | id2 => QuizTakerId
def save(request,id1,id2):
    
    if request.method=='POST':
        optedAnswer = request.POST['opted']
        timetaken = request.POST.get('timer')
        
        if type(timetaken)!=type(int):
            timetaken=0
        else:
            timetaken=int(timetaken)
            
        #Fetching respective object to create a response object
        questionObj = Question.objects.get(pk=id1)
        quizTakerObj = quizTaker.objects.get(pk=id2)
        
        #check if answer has been already recorded!
        obj = Response.objects.filter(quizQuestionId=questionObj,quizTakerId=quizTakerObj)
        
        if obj.exists():
            messages.info(request,'You can submit more than once')
        else:
            responseobj = Response(quizQuestionId=questionObj,quizTakerId=quizTakerObj,SelectedOption=optedAnswer,user=request.user)
            responseobj.save()
            quizTakerObj.totaltime+=timetaken
            quizTakerObj.save()
            #verify answer with original answer
            if int(optedAnswer) == questionObj.answer:
                quizTakerObj.score+=1
                quizTakerObj.save()
                                
        qset=questionObj.quizSetId
        qobj=QuizSet.objects.get(quizName=qset)
        id1=qobj.quizSetId
        #id1 => QuizSetId | id2 => QuizTakerId
        print('---------before redirect-------------------',id1,id2)
        return redirect(runquiz,id1,id2)

def endquiz(request,id1):
    quizTakerObj = quizTaker.objects.get(pk=id1)
    quizTakerObj.isCompleted=True
    if int(quizTakerObj.score) >= 6:
        quizTakerObj.isPassed=True
    quizTakerObj.save()
    return redirect(home)

def results(request):
    resultObj = quizTaker.objects.filter(user=request.user)
    con={}
    for obj in resultObj:
        print(obj)
        quizname = obj.quizSetAttempted.quizName
        score = obj.score
        print(quizname,score,obj.AttemptedTime)
        con[obj.AttemptedTime]=(quizname,score)
    table={}
    table['Quiz']=con
    return render(request,'result.html',table)
