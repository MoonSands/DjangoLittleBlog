from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from .models import *



def index(request):
    posts=feed.objects.all()
    context = {'posts':posts}
    return render(request, 'article_feed/index.html',context)

def article(request,article_id):
    art= get_object_or_404(feed, pk=article_id)
    context = {'title':art.title,
               'date':art.time_create,
               'content':art.content}
    return render(request, 'article_feed/article_single.html',context)

def pageNotFound(request, exception):
    return HttpResponseNotFound(render(request, 'article_feed/pageNotFound.html'))