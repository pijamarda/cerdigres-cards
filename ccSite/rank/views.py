from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.models import User

from .models import Rulebook, RulebookForm

def index(request):
    #nothing to be done here yet
    print("hola")

def rulebook_list(request):
    #return HttpResponse("Hola ya funciona la pagina")
    rulebook_list = Rulebook.objects.order_by('-create_date')[:5]
    #output = ', '.join([q.name for q in rulebook_list])
    #return HttpResponse(output)
    context = {'rulebook_list': rulebook_list}
    return render(request, 'rank/rulebook_list.html', context)

def rulebook_detail(request, rulebook_id):
    rulebook = get_object_or_404(Rulebook, pk=rulebook_id)
    return render(request, 'rank/rulebook_detail.html', {'rulebook': rulebook})

@login_required
def rulebook_create(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RulebookForm(request.POST)
        # check whether it's valid:
        if form.is_valid():            
            new_rulebook = form.save(commit=False)
            current_user = request.user
            new_rulebook.owner = current_user
            new_rulebook.general_votes = 0
            new_rulebook.valor_hot = 0
            new_rulebook.valor_new = 0
            new_rulebook.create_date = timezone.now()
            new_rulebook.modified_date = timezone.now()
            new_rulebook.save()
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RulebookForm()

    return render(request, 'rank/rulebook_create.html', {'form': form})
    
