from django.urls import path
from .views import *

urlpatterns=[
    path('', index, name='main'),
    path('article/<int:article_id>', article, name='article'),
]