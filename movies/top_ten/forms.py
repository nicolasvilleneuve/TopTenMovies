from django import forms

from .models import Movie

class MovieCreateForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = [
            'id',
            'title',
            'year',
            'description',
            'rating',
            'ranking',
            'review',
            'img_url',
            'owner'
        ]
