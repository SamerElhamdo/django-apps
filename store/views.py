from django.shortcuts import render, HttpResponse
from .forms import ProdectForm
from .models import Prodect
from django.utils import timezone
from django.db.models import F, DecimalField
from django.db.models.functions import Upper


import nexmo



# Create your views here.

def home_view(request):
    '''
    client = nexmo.Client(key='1f93f6f9', secret='Hl9qBYqcH5CjGka6')
    response = client.start_verification(
        number="905538013881",
        brand="Nexmo",
        code_length="4")

    if response["status"] == "0":
        print("Started verification request_id is %s" % (response["request_id"]))
    else:
        print("Error: %s" % response["error_text"])
    '''
    if request.method == 'POST':
        prodectForm = ProdectForm(request.POST, request.FILES)
        if prodectForm.is_valid():
            prodectForm.save()  
            prodectForm = ProdectForm()
            return render(request, 'store/index.html', {'prodectForm': prodectForm})
        else:
            return HttpResponse('hi rrr')
    
    else:
        prodectForm = ProdectForm()
        return render(request, 'store/index.html', {'prodectForm': prodectForm})

    
    
    #return HttpResponse("Hello World!")

def list_view(request):
    
    prodects = Prodect.objects.all()

    return render(request, 'store/list.html', {'prodects': prodects})
