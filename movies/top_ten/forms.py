from django import forms

from .models import Movie, User

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

class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'password'
        ]
