from django.shortcuts import render, get_object_or_404
from .models import Place, Review

def home(request):
    places = Place.objects.all()  # Fetch all places from the database
    reviews = Review.objects.all()[:5]  # Fetch the latest 5 reviews
    return render(request, 'places/home.html', {'places': places, 'reviews': reviews})

def place_detail(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    place_reviews = place.reviews.all()  # Fetch reviews related to this place
    context = {
        'place': place,
        'reviews': place_reviews,
    }
    return render(request, 'places/place_detail.html', context)

def search_view(request):
    query = request.GET.get('q')
    results = Place.objects.filter(name__icontains=query) if query else []
    return render(request, 'places/search_results.html', {'results': results, 'query': query})
