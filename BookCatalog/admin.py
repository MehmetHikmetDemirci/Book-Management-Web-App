from django.contrib import admin
from .models import Book

admin.site.site_header = 'My Bookstore Admin'
admin.site.site_title = 'Bookstore Admin Portal'
admin.site.index_title = 'Welcome to the Bookstore Admin'

admin.site.register(Book)