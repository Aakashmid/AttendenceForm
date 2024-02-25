from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .models import Condidate
from datetime import datetime
# Create your views here.


# ssss1234
def home(request,condidate_id=None):
    # return HttpResponse('Home page')
        
    if request.user.is_anonymous:
        return render(request,'app/login.html')
    elif condidate_id: 
        condidate=Condidate.objects.get(id=condidate_id)
        condidates=Condidate.objects.all()
        return render(request,'app/index.html',{'condidate':condidate,'Condidates':condidates})
    else:
        if request.method=="POST":
            name=request.POST.get('name')
            f_name=request.POST.get('fname')
            p_name=request.POST.get('pname')
            service_type=request.POST.get('service')
            if Condidate.objects.filter(user=request.user).exists():
                condidate=Condidate.objects.get(user=request.user)
                if condidate.Entrytime == condidate.Exittime:
                    Encondidate=Condidate.objects.get(user=request.user)
                    entryTime=Encondidate.Entrytime
                    Encondidate.delete()
                    condidate=Condidate(user=request.user,name=name,fname=f_name,pname=p_name,serviceType=service_type,Entrytime=entryTime)
                    condidate.save()
                    messages.success(request,'Exited !!')
                    # logout(request)
                    return HttpResponseRedirect(reverse("app:Home"))
                else:
                    messages.error(request,"You Aleready Exited !!")
                    return HttpResponseRedirect(reverse("app:Home"))

            else:
                condidate=Condidate(user=request.user,name=name,fname=f_name,pname=p_name,serviceType=service_type)
                condidate.save()
                messages.success(request,'Entered !!')
                return HttpResponseRedirect(reverse("app:Home",args=(condidate.id,)))
        else:
            condidates=Condidate.objects.all()
            return render(request,'app/index.html',{'Condidates':condidates})
    
def loginhand(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user_authenticated=authenticate(username=username,password=password)
        if user_authenticated:
            login(request,user_authenticated)
            messages.success(request,'Logged in successfully')
            return HttpResponseRedirect(reverse("app:Home"))
        else:
            messages.error(request,'Username or password is wrong')
            return render(request,'app/login.html')
    else:
        return render(request,'app/login.html')
def logouthand(request):
    logout(request)
    messages.success(request,"Successsfully logout !!")
    return redirect('/')

def createuser(request,username='',password=""):
    if (len(username)>1 and len(password)>1):
        if User.objects.filter(username=username).exists():
            messages.error(request,'Username is alerdy taken')
            return render(request,'app/login.html')
        else:
            user=User(username=username,password=password)
            user.save()
            login(request,user)
            messages.success(request,'User is created successfully !!')
            condidates=Condidate.objects.all()
            return render(request,'app/index.html',{'Condidates':condidates})
    else:
        messages.error(request,'Please enter username and password ')
        return render(request,'app/login.html')