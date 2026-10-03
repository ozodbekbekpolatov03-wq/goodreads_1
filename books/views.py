from django.shortcuts import render
from django.views import View
from books.models import Book

def landing_page(request):
    # print(request.COOKIES['example_cookie'])
    return render(request, 'landing.html')

class BooksView(View):
    def get(self, request):
        books = Book.objects.all()
        context = {
            'books': books
        }
        return render(request, 'books/list.html', context)

class BookDetailView(View):
    def get (self, request, id):
        book=Book.objects.get(id=id)
        
        context = {
            'book': book
        }
        return render(request, 'books/detail.html', context)