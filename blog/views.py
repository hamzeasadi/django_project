from django.shortcuts import render, HttpResponse
from . import models as m


def home(request):
    posts = m.Post
    context = {'postsss': posts.objects.all()}
    return render(request, 'blog/home.html', context=context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})
