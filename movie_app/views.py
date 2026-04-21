from django.shortcuts import render,redirect
from .models import Movie
from django.contrib.auth import login, logout, authenticate
from .forms import RegisrtationForm,LoginForm

def home(request):
    items = Movie.objects.all()
    return render(request, 'home.html', {'kinolar': items})



def registrciya(request):
    if request.method=='POST':
        formalar = RegisrtationForm(request.POST)
        if formalar.is_valid():
            user = formalar.save()
            login(request,user)
            return redirect('home')
        else:
            print(formalar.errors)
    else:
        formalar = RegisrtationForm()
    return render(request,'regis.html',{'formalar':formalar})


def kiriw(request):
    if request.method=='POST':
        formalar = LoginForm(request.POST)
        if formalar.is_valid():
            user = formalar.get_user()
            login(request,user)
            return redirect('home')
    else:
        formalar = LoginForm()
    return render(request,'login.html',{'formalar':formalar})


def log_out(request):
    logout(request)
    return redirect('home')