from django.shortcuts import render, redirect, get_object_or_404
from .models import Review
from movie.models import Movie
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm
from django.db.models import Avg

# Create your views here.

def review_list(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    reviews = movie.reviews.all() 
    return render(request, 'review/review_list.html', {'movie': movie, 'reviews': reviews})

@login_required(login_url='common:login')
def review_create(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            review.user = request.user
            review.save()
            
            movie.total = movie.reviews.aggregate(Avg('rating'))['rating__avg']
            movie.save()
            return redirect('review:review_list', movie_id=movie.id)
    else:
        form = ReviewForm()
    return render(request, 'review/review_create.html', {'form': form, 'movie': movie})

@login_required(login_url='common:login')
def review_delete(request, movie_id, review_id):
    review = get_object_or_404(Review, id=review_id, movie_id=movie_id)

    if review.user != request.user:
        return redirect('review:review_list', movie_id=movie_id) 

    review.delete()
    return redirect('review:review_list', movie_id=movie_id)
