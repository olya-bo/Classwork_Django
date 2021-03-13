"""Classwork_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from myapp.views import index, main_article, uniq_article, article, form_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),
    path('', index, name='index'),
    path('article/', main_article, name='mail_article'),
    path('article/33/', uniq_article, name='uniq_article'),
    path('article/<int:article_id>/', article, name='article'),
    path('article/<int:article_id>/<slug:name>', article, name='article_name'),
    path('form-url/', form_view, name='form-view'),
]
