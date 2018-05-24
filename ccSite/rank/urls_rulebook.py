from django.urls import path
from django.urls import include, path

from . import views

app_name = 'rulebook'

urlpatterns = [
    path('', views.rulebook_list, name='rulebook_list'),
    path('<int:rulebook_id>/', views.rulebook_detail, name='rulebook_detail'),
    path('create/', views.rulebook_create, name='rulebook_create'),
        
]