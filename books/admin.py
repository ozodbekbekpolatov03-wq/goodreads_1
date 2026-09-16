from django.contrib import admin
from books.models import Book, Author, BookAuthor, BookReview
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'isbn')
    search_fields = ('title', 'description', 'isbn')
    list_filter = ('title',)

admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(BookAuthor)
admin.site.register(BookReview)
# Register your models here.
