from django.shortcuts import render, get_object_or_404
from .models import Place, Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

@login_required
def add_review(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.place = place
            review.user = request.user  # associate with logged-in user
            review.name = request.user.username  # or get from user profile
            review.save()
            return redirect('place_detail', place_id=place.id)
    else:
        form = ReviewForm()

    return render(request, 'places/add_review.html', {'form': form, 'place': place})
def home(request):
    places = Place.objects.all()  # Fetch all places from the database
    reviews = Review.objects.all()[:5]  # Fetch the latest 5 reviews
    return render(request, 'places/home.html', {'places': places, 'reviews': reviews})

# places/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Place
from .forms import ReviewForm

def place_detail(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    reviews = place.reviews.all()

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.place = place
                review.user = request.user
                review.name = request.user.username
                review.save()
                return redirect('place_detail', place_id=place.id)
        else:
            return redirect('login')
    else:
        form = ReviewForm()

    context = {
        'place': place,
        'reviews': reviews,
        'review_form': form,
    }
    return render(request, 'places/place_detail.html', context)

def search_view(request):
    query = request.GET.get('q')
    results = Place.objects.filter(name__icontains=query) if query else []
    return render(request, 'places/search_results.html', {'results': results, 'query': query})


def place_detail(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    place_reviews = place.reviews.all()
    
    if request.method == 'POST':
        if request.user.is_authenticated:
            review_form = ReviewForm(request.POST)
            if review_form.is_valid():
                new_review = review_form.save(commit=False)
                new_review.place = place
                new_review.user = request.user
                new_review.name = request.user.username
                new_review.save()
                return redirect('place_detail', place_id=place.id)
        else:
            return redirect('login')
    else:
        review_form = ReviewForm()

    context = {
        'place': place,
        'reviews': place_reviews,
        'review_form': review_form,
    }
    return render(request, 'places/place_detail.html', context)
