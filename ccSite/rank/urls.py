from django.urls import path
from django.urls import include, path

from . import views

app_name = 'rank'

urlpatterns = [
    path('', views.index, name='index'),
    path('rulebook/<int:rulebook_id>/', views.rulebook_detail, name='rulebook_detail'),
    
]