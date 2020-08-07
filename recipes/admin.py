from django.contrib import admin

from recipes.models import Author, Recipe

admin.site.register(Author)
admin.site.register(Recipe)

