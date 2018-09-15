from django.db import models
from django.urls import reverse

class Author(models.Model):
    GENDRE_CHOICES = (
        ('F', 'Female'), ('M', 'Male')
    )
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    birth_date = models.DateField()
    death_date = models.DateField(blank=True)
    country = models.CharField(max_length=20)
    gender = models.CharField(max_length=1, choices=GENDRE_CHOICES)

    def __str__(self):
        return self.first_name

class Genre(models.Model):
    name = models.CharField(max_length=120, help_text='Ented a book genre(e.g. Science Fiction)')
    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=120, help_text='Enter the name of the publisher')
    country = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Languages(models.Model):
    name = models.CharField(max_length=200, help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)")
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=120)
    summary = models.TextField(null=True, blank=True)
    author = models.ManyToManyField(Author)
    publisher = models.ManyToManyField(Publisher,  related_name='published')
    isbn = models.CharField('ISBN',  max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, help_text='Select a genre for this book')
    language = models.ForeignKey(Languages, on_delete=models.CASCADE,help_text="Select a language e.g. French, English...")

    def __str__(self):
        return self.name



