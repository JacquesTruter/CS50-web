# myapp/context_processors.py

from .forms import SearchForm

def My_SearchForm(request):
    return {'My_SearchForm': SearchForm()}