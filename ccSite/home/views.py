from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return HttpResponse("Hola ya funciona la pagina")
