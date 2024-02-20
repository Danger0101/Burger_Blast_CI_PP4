'''
This module contains the views for the about app.
'''
from django.shortcuts import render


def index_view(request):
    '''
    Renders the index page.
    '''
    context = {'active_page': 'index'}
    return render(request, 'about/index.html', context)


def about_view(request):
    '''
    Renders the about page.
    '''
    context = {'active_page': 'about'}
    return render(request, 'about/about.html', context)
