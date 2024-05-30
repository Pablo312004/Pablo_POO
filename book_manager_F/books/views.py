from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm
from django.core.paginator import Paginator

# Create your views here.


def book_list(request):
    book_list = Book.objects.all()
    paginator = Paginator(book_list, 10)  # Mostrar 10 livros por página

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "books/book_list.html", {"page_obj": page_obj})


def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "books/book_form.html", {"form": form})


def edit_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm(instance=book)
    return render(request, "books/book_form.html", {"form": form})
