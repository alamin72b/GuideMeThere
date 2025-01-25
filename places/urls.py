from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # homepage
    path('place/<int:place_id>/', views.place_detail, name='place_detail'),
    path('search/', views.search_view, name='search'),  # Add this line

]
