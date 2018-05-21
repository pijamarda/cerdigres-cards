from django.urls import path
from django.urls import include, path

from . import views

app_name = 'rank'

urlpatterns = [
    path('', views.rulebook_list, name='index'),    
    
]