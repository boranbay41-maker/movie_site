from django.contrib import admin
from .models import Actors,Movie,Languages,Comment,Genres,Country,CustomUser

admin.site.register(CustomUser)
admin.site.register(Languages)
admin.site.register(Comment)
admin.site.register(Genres)
admin.site.register(Country)
admin.site.register(Actors)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'has_film_video')
    search_fields = ('title', 'desc')
    filter_horizontal = ('actors', 'countries', 'languages', 'genres')
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'year', 'desc', 'image', 'trailer')
        }),
        ('Видео', {
            'fields': ('film',),
            'description': 'Загрузите видеофайл фильма (рекомендуемые форматы: MP4, WebM, OGG)'
        }),
        ('Связи', {
            'fields': ('actors', 'countries', 'languages', 'genres')
        }),
    )
    
    def has_film_video(self, obj):
        return 'Да' if obj.film else 'Нет'
    has_film_video.short_description = 'Есть видео'
