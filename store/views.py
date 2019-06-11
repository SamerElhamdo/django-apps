from django.shortcuts import render, HttpResponse
from .forms import ProdectForm
from .models import Prodect, Discount
from django.utils import timezone
from django.db.models import F, DecimalField


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
            return render(request, 'index.html', {'prodectForm': prodectForm})
        else:
            return HttpResponse('hi rrr')
    
    else:
        prodectForm = ProdectForm()

        return render(request, 'index.html', {'prodectForm': prodectForm})

    
    
    #return HttpResponse("Hello World!")

def list_view(request):
    
    prodects = Prodect.objects.all()
    for prodect in prodects:
        discount_percentage = Discount.objects.filter(product_id=prodect.id).first()
        prodect = Prodect.objects.filter(id=prodect.id).annotate(new_price=F('price')*discount_percentage)


    return render(request, 'list.html', {'prodects': prodects})
