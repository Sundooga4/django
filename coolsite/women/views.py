from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect

from .models import *


def index(request):
    posts = Women.objects.all()
    context = {
        'posts': posts,
        'title': 'Main page',
        'cat_selected':0,
    }
    return render(request, 'women/index.html', context=context)

def about(request):
    return render(request, 'women/about.html', {'title': 'About site'})

def addpage(request):
    return render(request, 'women/about.html', {'title': 'Add page'})

def contact(request):
    return render(request, 'women/about.html', {'title': 'Feedback'})

def login(request):
    return HttpResponse('Authorization')


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)

    context = {
        'post': post,
        'title': post.title,
        'cat_selected': post.cat_id,
    }

    return render(request, 'women/post.html', context=context)

def show_category(request, cat_slug):
    cat = Category.objects.filter(slug=cat_slug)
    posts = Women.objects.filter(cat_id=cat[0].id)

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'title': 'Category filter',
        'cat_selected': cat[0].id,
    }
    return render(request, 'women/index.html', context=context)


def pageNotFound(request,exception):
    return HttpResponseNotFound("<h1>There is no such page</h1>")
