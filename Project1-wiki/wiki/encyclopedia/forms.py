# myapp/forms.py

from django import forms

class SearchForm(forms.Form):
    search = forms.CharField(widget=forms.TextInput(attrs={'class': 'search', 'placeholder': 'Search'}))
   