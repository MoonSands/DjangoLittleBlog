from django.shortcuts import render
from .models import *


def index(request):
    posts=feed.objects.all()
    context = {'posts':posts}
    return render(request, 'article_feed/index.html',context)

def article(request,article_id):
    art=feed.objects.get(pk=article_id)
    context = {'title':art.title,
               'date':art.time_create,
               'content':art.content}
    return render(request, 'article_feed/article_single.html',context)