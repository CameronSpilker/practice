from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django_mako_plus import view_function
from datetime import datetime
from homepage import models as cmod
from django.contrib.auth.decorators import login_required, permission_required
from .. import dmp_render, dmp_render_to_string
from django.contrib.postgres.search import SearchVector
from django import forms
import operator

@view_function
def process_request(request):
    # #GET.get will return none and not an error
    # print('>>>>', request.GET.get('user_search'))


    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            print('>>>> FORM CHECKS OUT')
            print('DATA', form.cleaned_data)
            search = form.cleaned_data.get('search')
            print('>>>> SEARCH', search)
            quotes = cmod.Category.objects.annotate(search=SearchVector('author') + SearchVector('quote') + SearchVector('tags')).filter(search__icontains=search)
            print('>>>>>> QUOTES', quotes)
            context = {
                'quotes': quotes,
                'form': form,
            }
            return dmp_render(request, 'index.html', context)
        return HttpResponseRedirect('/')
    else:
        form = SearchForm()

    quotes = cmod.Category.objects.all()

    print('>>>>>>>>>>', quotes)

    context = {
        'quotes': quotes,
        'form': form,
    }
    return dmp_render(request, 'index.html', context)

class SearchForm(forms.Form):

    search = forms.CharField(label="", required=False)

    def clean_searchResults(self):
        search = self.cleaned_data.get('search')
        print('search resutls here:', search)

        return search

# @view_function
# def search(request):
#     try:
#         print('>>>>>>This is in the url', request.urlparams[0])
#         userSearch = request.urlparams[0]
#         quotes = cmod.Category.objects.annotate(search=SearchVector('author') + SearchVector('quote') + SearchVector('tags')).filter(search__icontains=userSearch)
#         # quotes = cmod.Category.objects.filter(cmod.Category(author__icontains=userSearch) | cmod.Category(quote__icontains=userSearch) | cmod.Category(tags__icontains=userSearch))
#         print('>>>>>>>>>>', quotes)
#     except (TypeError, cmod.Category.DoesNotExist):
#         return HttpResponseRedirect('/homepage/index/')
#     for q in quotes:
#         print('This is the id:', q.id)
#         print('This is the author:', q.author)
#         print('This is the quote: ', q.quote)
#         print('This is the tags:', q.tags)

#     context = {
#         'quotes': quotes,
#     }
#     return dmp_render(request, 'index.html', context)