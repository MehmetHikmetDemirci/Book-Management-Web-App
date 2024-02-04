from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('book/add/', views.book_add, name='book_add'),
    path('book/edit/<int:pk>/', views.book_edit, name='book_edit'),
    path('book/delete/<int:pk>/', views.book_delete, name='book_delete'),  # Kitap silme URL'i
]
