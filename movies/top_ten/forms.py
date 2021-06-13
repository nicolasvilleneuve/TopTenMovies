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
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder": "Email"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Confirm Password"}))

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]

