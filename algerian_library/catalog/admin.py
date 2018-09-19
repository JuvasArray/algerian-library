from django.contrib import admin
from catalog.models import Author, Book, Genre, Language, Publisher

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_search = ['first_name']
    list_display = ('last_name', 'first_name', 'birth_date', 'death_date')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'display_author', 'display_genre']

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_search = ['name']
    list_display = ['name']
