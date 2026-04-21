from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('reg/',views.registrciya,name='registration'),
    path('login/', views.kiriw, name='log_in'),
    path('logout/',views.log_out,name='logout')
]
