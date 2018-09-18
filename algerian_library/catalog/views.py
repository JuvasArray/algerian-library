from django.shortcuts import render
from catalog.models import Author, Book,BookInstance, Genre, Language, Publisher

def index(request):
    number_of_books = Book.objects.all().count()
    number_of_instances = BookInstance.objects.all().count()
    number_of_available_instances = BookInstance.objects.filter(status__exact='AV')
    number_of_authors = Author.objects.all()

    context = {
            'number_of_books': number_of_books,
            'number_of_instances': number_of_instances,
            'number_of_available_instances': number_of_available_instances,
            'number_of_authors': number_of_authors,
            }
    return render(request, 'catalog/index.html', context)
