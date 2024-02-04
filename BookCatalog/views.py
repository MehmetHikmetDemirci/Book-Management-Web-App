from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm
from django.contrib.auth.decorators import login_required, permission_required

# Kitap listesini göster
@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, 'BookCatalog/book_list.html', {'books': books})

# Kitap detaylarını göster
@login_required
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'BookCatalog/book_detail.html', {'book': book})

# Yeni kitap ekleme
@login_required
@permission_required('BookCatalog.add_book', raise_exception=True)
def book_add(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'BookCatalog/book_form.html', {'form': form})

# Kitap düzenleme
@login_required
@permission_required('BookCatalog.change_book', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'BookCatalog/book_form.html', {'form': form})

# Kitap silme
@login_required
@permission_required('BookCatalog.delete_book', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'BookCatalog/book_confirm_delete.html', {'book': book})
