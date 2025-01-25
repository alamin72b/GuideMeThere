from django.db import models
from django.contrib.auth.models import User

class Place(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='place_images/', null=True, blank=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)
    rating = models.PositiveSmallIntegerField(default=5)  # Rating out of 5
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']  # Newest reviews first

    def __str__(self):
        return f"Review by {self.name} for {self.place.name}"
