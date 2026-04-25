from django.contrib import admin
from .models import Actors,Movie,Languages,Comment,Genres,Country,CustomUser

admin.site.register(CustomUser)
admin.site.register(Movie)
admin.site.register(Actors)
admin.site.register(Languages)
admin.site.register(Comment)
admin.site.register(Genres)
admin.site.register(Country)
