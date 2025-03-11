"""
URL configuration for chaiaurDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))     # the '/' is important!!
"""

from django.contrib import admin     # importing admin from django.contrib  
from django.urls import path, include        # importing path from django.urls
from . import views                 # importing views from .

urlpatterns = [
    path("admin/", admin.site.urls),    # importing admin from django.contrib
    path('', views.index , name='index'),    
    path('about/', views.about , name='about'),   
    path('contact/', views.contact , name='contact'), 
    path('chai/', include('chai.urls')),    # importing chai from chai.urls



    path("__reload__/", include("django_browser_reload.urls")),    # Always put at last in the urlpatterns
]
