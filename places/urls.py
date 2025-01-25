from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('place/<int:place_id>/', views.place_detail, name='place_detail'),
    path('search/', views.search_view, name='search'),
    # New path for adding reviews
    path('place/<int:place_id>/review/', views.add_review, name='add_review'),
]
