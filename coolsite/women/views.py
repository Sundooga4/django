from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.views.generic import ListView


from .forms import *
from .models import *

class WomenHome(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    extra_context = {'title': 'Main page'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Women.objects.filter(is_published=True)
'''
def index(request):
    posts = Women.objects.all()
    context = {
        'posts': posts,
        'title': 'Main page',
        'cat_selected':0,
    }
    return render(request, 'women/index.html', context=context)
'''
def about(request):
    return render(request, 'women/about.html', {'title': 'About site'})

def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()
    return render(request, 'women/addpage.html', {'form': form, 'title': 'Add page'})

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

class WomenCategory(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Category' + str(context['posts'][0].cat)
        context['cat_selected'] = context['posts'][0].cat_id
        return context

    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)



'''
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
'''

def pageNotFound(request,exception):
    return HttpResponseNotFound("<h1>There is no such page</h1>")
