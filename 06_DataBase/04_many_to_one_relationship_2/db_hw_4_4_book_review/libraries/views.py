from django.shortcuts import render, redirect
from .models import Book, Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'libraries/index.html', context)

def detail(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    reviews = book.review_set.all()
    form = ReviewForm()
    context = {
        'book': book,
        'form': form,
        'reviews': reviews,
    }
    return render(request, 'libraries/detail.html', context)

@login_required
def create_review(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.book = book
            review = form.save()
            return redirect('libraries:detail', book_pk)
    else:
        form = ReviewForm()
    context = {
        'book': book,
        'form': form,
    }
    return render(request, 'libraries:detail', context)

@login_required
def delete_review(request, book_pk, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.user == review.user:
        review.delete()
    return redirect('libraries:detail', book_pk)