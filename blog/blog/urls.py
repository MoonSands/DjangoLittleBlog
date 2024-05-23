"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from article_feed.views import *
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('', index, name='main'),
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls')),
    path('api/post/', PostAPIView.as_view()),
    path('api/post/create', PostCreateAPIView.as_view()),
    path('api/post/<int:pk>', PostUPdateDeleteAPIView.as_view()),
    path('api/docs/', DocsAPIView.as_view()),
    path('api/docs/create', DocsCreateAPIView.as_view()),
    path('api/docs/<int:pk>', DocsUPdateDeleteAPIView.as_view()),
    path('api/products/', ProductAPIView.as_view()),
    path('api/products/create', ProductCreateAPIView.as_view()),
    path('api/products/<int:pk>', ProductUPdateDeleteAPIView.as_view()),
    path('api/faq/', FAQAPIView.as_view()),
    path('api/faq/create', FAQCreateAPIView.as_view()),
    path('api/faq/<int:pk>', FAQUPdateDeleteAPIView.as_view()),
    path('api/forms/', DataFromFormsAPIView.as_view()),
    path('api/forms/<int:pk>', DataFromFormsSingleAPIView.as_view()),

]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)