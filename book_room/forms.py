from django import forms
from .models import Review


class RoomReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['room', 'review_content']