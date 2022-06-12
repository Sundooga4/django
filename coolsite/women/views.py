from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect

from .models import *

menu = ['About site', 'Add article', 'Contact us', 'Log in']

def index(request):
    posts = Women.objects.all()
    return render(request, 'women/index.html', {'posts': posts, 'menu': menu, 'title': 'Main page'})

def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'About site'})

def categories(request, catid):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Articles by category</h1><p>{catid}</p>")

def archive(request, year):
    if int(year) > 2020:
        return redirect('mainpage', permanent=True)

    return HttpResponse(f"<h1>Archive by year</h1><p>{year}</p>")

def pageNotFound(request,exception):
    return HttpResponseNotFound("<h1>There is no such page</h1>")