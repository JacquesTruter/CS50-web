from django.shortcuts import render
from markdown2 import Markdown
from .forms import SearchForm
from . import util

def convert_md_to_html(title):
    content = util.get_entry(title)
    markdowner = Markdown()
    if content == None:
        return None
    else:
        return markdowner.convert(content)

def index(request): 
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):   
    html_content = convert_md_to_html(title)
    if html_content == None:
        return render(request, "encyclopedia/error.html", {
            "erroCode": 404,
            "errorMessage": title + " page not found"
        })
    else:
        return render(request, "encyclopedia/entry.html", {
                      "title": title,
                      "entryContent": html_content})


def search(request):
    # Check if method is POST
    if request.method == "POST":

        # Take in the data the user submitted and save it as form
        form = SearchForm(request.POST)

        # Check if form data is valid (server-side)
        if form.is_valid():

            # Isolate the search_entry from the 'cleaned' version of form data
            search_entry = form.cleaned_data["search"]

            html_content = convert_md_to_html(search_entry)
            
            if html_content == None:
                match_list = [] 
                entries = util.list_entries()

                for entry in entries:
                    if search_entry.lower() in entry.lower():
                        match_list.append(entry)
                print(match_list) 
                return render(request, "encyclopedia/search.html", {
                            "match_list": match_list})
            else:
                return render(request, "encyclopedia/entry.html", {
                    "title": search_entry,
                    "entryContent": html_content})
        else:

            # If the form is invalid, re-render the page with existing information.
            return render(request, "encyclopedia/search.html")

    return render(request, "encyclopedia/search.html")