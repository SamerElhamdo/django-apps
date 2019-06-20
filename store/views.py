from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .forms import ProductForm, OrderForm
from .models import Product, Order
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
    products = Product.objects.all()

    return render(request, 'store/list.html', {'products': products})


    
    
    #return HttpResponse("Hello World!")

def product_form(request):

    if request.method == 'POST':
        productForm = ProductForm(request.POST, request.FILES)
        if productForm.is_valid():
            productForm.save()  
            productForm = ProductForm()
            return render(request, 'store/new-product.html', {'productForm': productForm})
        else:
            return HttpResponse('hi rrr')
    
    else:
        prodectForm = ProdectForm()
        return render(request, 'store/index.html', {'prodectForm': prodectForm})



def order_form(request, product_id):
    product = get_object_or_404(Product,pk=product_id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.cleaned_data['color'] = request.POST.get('color')
            form.cleaned_data['size'] = request.POST.get('size')
            
            form.save()
            return redirect('/')
    else:
        form = OrderForm(initial = {'product': product_id})
    context = {
        'form': form,
        'product':product,
    }
    return render(request, 'store/new-order.html', context)