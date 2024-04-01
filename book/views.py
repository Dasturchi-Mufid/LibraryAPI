from django.views.generic import ListView
from . import models

class BookListView(ListView):
    model = models.Book
    template_name = 'books/book_list.html'
