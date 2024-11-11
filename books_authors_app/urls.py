from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('books', views.books),
    path('book/<int:id>', views.view_book),
    path('authors', views.authors),
    path('author/<int:id>', views.view_author),
    path('createBook', views.create_book),
    path('createAuthor', views.create_author),

]