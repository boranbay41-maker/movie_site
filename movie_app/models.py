from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone_num = models.CharField(max_length=13, verbose_name="Номер телефона")
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, verbose_name="Аватар")


from django.contrib.auth import get_user_model

User = get_user_model()


class Actors(models.Model):
    name = models.CharField(max_length=50)
    sure_name = models.CharField(max_length=50)
    bio = models.TextField()
    birth_date = models.DateField()
    
    def __str__(self):
        return self.name
    
    
class Country(models.Model):
    country = models.CharField(max_length=50)
    
    def __str__(self):
        return self.country
  
    
class Genres(models.Model):
    genre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.genre
    
    
class Languages(models.Model):
    language = models.CharField(max_length=50)   
    
    def __str__(self):
        return self.language
    
    
class Movie(models.Model):
    title = models.CharField(max_length=255)
    year = models.TextField()
    image = models.ImageField(upload_to='movies/')
    desc = models.TextField()
    trailer = models.URLField()
    film = models.FileField()
    actors = models.ManyToManyField(Actors)
    countries = models.ManyToManyField(Country)
    languages = models.ManyToManyField(Languages)
    genres = models.ManyToManyField(Genres)
    
    def __str__(self):
        return self.title
    
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

 


