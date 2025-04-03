from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializer import BookSerializer

class BooksListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
