from django.shortcuts import render
from .models import *


def index(request):
    posts=feed.objects.all()
    return render(request, 'article_feed/index.html',{'posts':posts})

def article(request,article_id):
    art=feed.objects.get(pk=article_id)
    return render(request, 'article_feed/article_single.html',{'title':art.title,
                                                  'date':art.time_create,
                                                  'content':art.content})