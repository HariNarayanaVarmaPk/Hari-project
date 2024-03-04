from django import forms
from .models import Cinema


class CinemaForm(forms.ModelForm):
    CATEGORY_CHOICES = [
        ('Action', 'Action'),
        ('Comedy', 'Comedy'),
        ('Drama', 'Drama'),
        ('Horror', 'Horror')
    ]

    category = forms.ChoiceField(choices=[('', 'Select Category')] + CATEGORY_CHOICES)

    class Meta:
        model = Cinema
        fields = ['title', 'poster', 'description', 'release_date', 'actors', 'trailer_link', 'category']

class CinemaAdminForm(forms.ModelForm):
    class Meta:
        model = Cinema
        fields = ['title', 'poster', 'description', 'release_date', 'actors', 'trailer_link', 'category', 'added_by']
        
        
class CinemaViewForm(forms.ModelForm):
    class Meta:
        model = Cinema
        fields = ['title', 'poster', 'description', 'release_date', 'actors', 'category', 'trailer_link', 'added_by']
        