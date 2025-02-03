from django.shortcuts import render
from .models import Book
from django.views.generic import ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

class BookListView(ListView):
    model = Book
    context_object_name='book_list'
    template_name = 'books/book_list.html'
    login_url='account_login'
# Create your views here.

class BookDetailView(DetailView):
    model = Book
    context_object_name='book'
    template_name='books/book_detail.html'
    login_url='account_login'

class SearchResultsListView(ListView):
    model = Book
    template_name = 'books/search_results.html'
    context_object_name = 'book_list'

class SearchResultsListView(ListView):
    model = Book
    template_name = 'books/search_results.html'
    context_object_name = 'book_list'
    def get_queryset(self):
        query= self.request.GET.get('q')
        return Book.objects.filter(Q(title__icontains=query)|Q(author__icontains=query))