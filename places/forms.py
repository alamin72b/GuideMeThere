from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        # 'name' might be auto-filled if you want the user's name from the user model,
        # or you might let them type a display name. Adjust as needed.
