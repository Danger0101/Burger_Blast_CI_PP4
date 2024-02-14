from django.shortcuts import render
from django.http import HttpResponse

def index_view(request):
    context = {'active_page': 'index'}
    return render(request, 'about/index.html', context)

def about_view(request):
    context = {'active_page': 'about'}
    return render(request, 'about/about.html', context)
