from django import forms
from .models import Cinema

class CinemaForm(forms.ModelForm):
    class Meta:
        model = Cinema
        fields = ['title', 'poster', 'description', 'release_date', 'actors', 'category', 'trailer_link']

class CinemaViewForm(forms.ModelForm):
    class Meta:
        model = Cinema
        fields = ['title', 'poster', 'description', 'release_date', 'actors', 'category', 'trailer_link', 'added_by']
        