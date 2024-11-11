from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(default=" ")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Author(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    books = models.ManyToManyField(Book, related_name="authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    notes = models.TextField()
    
def get_all_books():
    return Book.objects.all()

def get_all_authors():
    return Author.objects.all()

def get_book_by_id(id):
    return Book.objects.get(id=id)

def get_author_by_id(id):
    return Author.objects.get(id=id)

def create_book(data):
    title = data['title']
    desc = data['desc']
    Book.objects.create(title=title, desc = desc)

def create_author(data):
    first_name = data['first_name']
    last_name = data['last_name']
    notes = data['notes']
    Author.objects.create(first_name=first_name, last_name=last_name, notes=notes)