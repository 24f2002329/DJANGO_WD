from django.urls import path        # importing path from django.urls
from . import views                 # importing views from .

#localhost:8000/chai/
#localhost:8000/chai/order/
urlpatterns = [
    path('', views.all_chai , name='all_home'),    # importing all_chai from views

]