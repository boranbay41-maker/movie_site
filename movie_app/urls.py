from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('reg/',views.registrciya,name='registration'),
    path('login/', views.kiriw, name='login'),
    path('logout/',views.log_out,name='logout'),
    path('comment/<int:movie_id>/', views.add_comment, name='add_comment'),
]
