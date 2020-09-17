from django.contrib import admin
from .models import Movie



class movieadmin(admin.ModelAdmin):
    list_display=("id","name","date")
    list_display_links=["name"]
    list_filter=["date"]
    search_fields=("name","desc")
    list_per_page=10


# Register your models here.
admin.site.register(Movie,movieadmin)