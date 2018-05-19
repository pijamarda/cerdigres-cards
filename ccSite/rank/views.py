from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Rulebook

def index(request):
    #return HttpResponse("Hola ya funciona la pagina")
    rulebook_list = Rulebook.objects.order_by('-create_date')[:5]
    #output = ', '.join([q.name for q in rulebook_list])
    #return HttpResponse(output)
    context = {'rulebook_list': rulebook_list}
    return render(request, 'rank/index.html', context)

def rulebook_detail(request, rulebook_id):
    rulebook = get_object_or_404(Rulebook, pk=rulebook_id)
    return render(request, 'rank/rulebook_detail.html', {'rulebook': rulebook})
    
