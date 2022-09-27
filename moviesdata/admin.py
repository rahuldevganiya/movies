from django.contrib import admin


# Register your models here.
from .models import moviesdata

@admin.register(moviesdata)
class moviesAdmin(admin.ModelAdmin):
    list_display = ('title','released_year','rating','id','generes')
