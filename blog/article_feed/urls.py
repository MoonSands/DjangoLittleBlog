from django.urls import path
from .views import *

urlpatterns=[
    path('', index, name='main'),
    path('article/<slug:article_slug>', article, name='article'),
    path('categories/<str:name>', cats, name='category'),
]