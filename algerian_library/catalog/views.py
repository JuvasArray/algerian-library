from django.shortcuts import render
from catalog.models import Author, Book, Genre, Language, Publisher
def index(request):
    return render(request, 'catalog/index.html', {})
