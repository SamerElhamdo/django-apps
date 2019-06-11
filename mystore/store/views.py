from django.shortcuts import render, HttpResponse
from .forms import ProdectForm
from django.utils import timezone



# Create your views here.

def home_view(request):
    if request.method == 'POST':
        prodectForm = ProdectForm(request.POST, request.FILES)
        if prodectForm.is_valid():
            prodectForm.save()  
            prodectForm = ProdectForm()
            return render(request, 'index.html', {'prodectForm': prodectForm})
        else:
            return HttpResponse('hi rrr')
    
    else:
        prodectForm = ProdectForm()

        return render(request, 'index.html', {'prodectForm': prodectForm})

    
    #return HttpResponse("Hello World!")
