from django.shortcuts import render,redirect,get_object_or_404
from .models import Movie,Comment
from django.contrib.auth import login, logout, authenticate
from .forms import CommentForm, RegisrtationForm,LoginForm
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

def home(request):
    poisk = request.GET.get('q')
    if poisk:
        search_words = [w for w in poisk.split() if w]
        if len(search_words) >= 2:
            actor_filter = (
                Q(actors__name__icontains=search_words[0], actors__sure_name__icontains=search_words[-1]) |
                Q(actors__name__icontains=search_words[-1], actors__sure_name__icontains=search_words[0])
            )
        else:
            actor_filter = (
                Q(actors__name__icontains=poisk) |
                Q(actors__sure_name__icontains=poisk)
            )
        items = Movie.objects.filter(
            Q(title__icontains=poisk) | 
            actor_filter |
            Q(countries__country__icontains=poisk) |
            Q(genres__genre__icontains=poisk) |
            Q(languages__language__icontains=poisk)
        ).distinct()
    else:
        items = Movie.objects.all()
    
    paginator = Paginator(items, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'home.html', {'kinolar': page_obj, 'page_obj': page_obj})


def product_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    comments = Comment.objects.filter(movie=movie)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user        
            comment.movie_id = pk        
            comment.save()
    return render(request, 'product_detail.html', {'movie': movie, 'comments': comments, 'form': CommentForm()})



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


@login_required  
def add_comment(request, movie_id):
                      
    return redirect('product_detail', pk=movie_id)