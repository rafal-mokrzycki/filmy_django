from django.contrib import admin
from .models import Film

# admin.site.register(Film)

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    fields = ["tytul"]