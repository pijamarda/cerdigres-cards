from django.urls import path
from django.urls import include, path

from . import views

app_name = 'rulebook'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:rulebook_id>/', views.rulebook_detail, name='rulebook_detail'),
    
]