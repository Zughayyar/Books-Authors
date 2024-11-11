from django.shortcuts import render, redirect
from . import models


def index(request):
    return render(request, "index.html")

def books(request):
    context = {
        'books' : models.get_all_books()
    }
    return render(request, "book_add.html", context)

def view_book(request, id):
    context = {
        'book' : models.get_book_by_id(id),
    }
    return render(request, "book_view.html", context)

def authors(request):
    context = {
        'authors' : models.get_all_authors()
    }
    return render(request, 'author_add.html', context)

def view_author(request, id):
    context = {
        'author' : models.get_author_by_id(id)
    }
    return render(request, "author_view.html", context)

def create_book(request):
    if request.method == "POST":
        models.create_book(request.POST)
    return redirect('/books')

def create_author(request):
    if request.method == "POST":
        models.create_author(request.POST)
    return redirect('/authors')