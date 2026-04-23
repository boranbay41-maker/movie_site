from django.shortcuts import render,redirect,get_object_or_404
from .models import Movie
from django.contrib.auth import login, logout, authenticate
from .forms import RegisrtationForm,LoginForm
from django.db.models import Q

def home(request):
    poisk = request.GET.get('q')
    if poisk:
        items = Movie.objects.filter(
            Q(title__icontains=poisk) | 
            Q(actors__name__icontains=poisk) |
            Q(actors__sure_name__icontains=poisk) |
            Q(countries__country__icontains=poisk) |
            Q(genres__genre__icontains=poisk)
        )
    else:
        items = Movie.objects.all()
    return render(request, 'home.html', {'kinolar': items})


def product_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'product_detail.html', {'movie': movie})



def registrciya(request):
    if request.method=='POST':
        formalar = RegisrtationForm(request.POST)
        if formalar.is_valid():
            user = formalar.save()
            login(request,user)
            return redirect('home')
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