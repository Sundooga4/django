from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect

from .models import *

menu = [{'title': "About site", 'url_name': 'about'},
        {'title': "Add article", 'url_name': 'add_page'},
        {'title': "Feedback", 'url_name': 'contact'},
        {'title': "Log in", 'url_name': 'login'}
]

def index(request):
    posts = Women.objects.all()
    cats = Category.objects.all()
    context = {
        'posts': posts,
        'cats':cats,
        'menu': menu,
        'title': 'Main page',
        'cat_selected':0,
    }
    return render(request, 'women/index.html', context=context)

def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'About site'})

def addpage(request):
    return HttpResponse('Add page')

def contact(request):
    return HttpResponse('Feedback')

def login(request):
    return HttpResponse('Authorization')


def show_post(request, post_id):
    return HttpResponse(f"Showing page with id={post_id}")

def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Category filter',
        'cat_selected': cat_id,
    }
    return render(request, 'women/index.html', context=context)


def pageNotFound(request,exception):
    return HttpResponseNotFound("<h1>There is no such page</h1>")
