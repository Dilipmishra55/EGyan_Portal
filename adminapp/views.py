from django . shortcuts import render, redirect
from django.views.decorators.cache import cache_control
from nouapp.models import Student,Login,Enquiry
from studentapp.models import Sturesponse
from . models import Material,News
from datetime import date
from django.contrib import messages
# Create your views here.
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def adminhome(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            return render(request,'adminhome.html',locals())
    except KeyError:
            return redirect('nouapp:login')
    return render(request,'adminhome.html')

def adminlogout(request):
    try:
        del request.session['adminid']
        return redirect('nouapp:login')
    except KeyError:
        return redirect('nouapp:login')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewstudent(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            stu=Student.objects.all()
            return render(request,'viewstudent.html',locals())
    except KeyError:
            return redirect('nouapp:login')
    return render(request,'adminhome.html')


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewenquiry(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            enq=Enquiry.objects.all()
            return render(request,'viewenquiry.html',locals())
    except KeyError:
            return redirect('nouapp:login')
    


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewfeedback(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            feed=Sturesponse.objects.filter(responsetype='feedback')
            return render(request,'viewfeedback.html',locals())
    except KeyError:
            return redirect('nouapp:login')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewcomplain(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            comp=Sturesponse.objects.filter(responsetype='complain')
            return render(request,'viewcomplain.html',locals())
    except KeyError:
            return redirect('nouapp:login')
    
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def uploadmaterial(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            if request.method=='POST':
                program=request.POST['program']
                branch=request.POST['branch']
                year=request.POST['year']
                subject=request.POST['subject']
                materialtype=request.POST['materialtype']
                filename=request.POST['filename']
                myfile=request.FILES['myfile']
                posteddate=date.today()
                mat=Material(program=program,branch=branch,year=year,subject=subject,materialtype=materialtype,filename=filename,myfile=myfile,posteddate=posteddate)
                mat.save()
                messages.success(request,'Material is Uploaded')
            return render(request,'uploadmaterial.html',locals())
    except KeyError:
            return redirect('nouapp:login')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def addnews(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            if request.method=='POST':
                newstext=request.POST['newstext']
                postdate=date.today()
                News(newstext=newstext,posteddate=postdate).save()
            nw=News.objects.all()
            return render(request,'addnews.html',locals())
    except KeyError:
            return redirect('nouapp:login')
    

def delnews(request,nid):
    News.objects.get(nid=nid).delete()
    return redirect('adminapp:addnews')

