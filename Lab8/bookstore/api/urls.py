from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BooksListView.as_view(), name='books-list'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='books-detail'),
]