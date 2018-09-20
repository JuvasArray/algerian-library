from django.shortcuts import render
from catalog.models import Author, Book, Genre, Language, Publisher
from django.views.generic import ListView

def index(request):
    number_of_books = Book.objects.all().count()
    number_of_authors = Author.objects.all().count()

    context = {
            'number_of_books': number_of_books, 
            'number_of_authors': number_of_authors,
            }
    return render(request, 'catalog/index.html', context)

class BookListView(ListView):
    model = Book

class AuthorListView(ListView):
    model = Author

