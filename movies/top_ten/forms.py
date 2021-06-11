from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]

