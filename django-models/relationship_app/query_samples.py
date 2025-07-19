import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = author.books.all()
    return books


def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

def get_librarian_of_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian
