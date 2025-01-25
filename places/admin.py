from django.contrib import admin
from .models import Place, Review

class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1
    readonly_fields = ('created_at',)

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [ReviewInline]

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'place', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('name', 'comment')
    readonly_fields = ('created_at',)
