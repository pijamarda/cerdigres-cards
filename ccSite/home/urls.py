from django.urls import path
from django.urls import include, path

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

from . import views
urlpatterns = [
    path('register/', CreateView.as_view(
            template_name='registration/register.html',
            form_class=UserCreationForm,
            success_url='/'
    )),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.index, name='index'),
]