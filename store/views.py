from django.shortcuts import render, HttpResponse, get_object_or_404, redirect, HttpResponseRedirect
from .forms import ProductForm, ProductAttributeForm, ImageForm, OrderForm, ProductDiscountForm
from .models import Product, Image, Order, ProductAttribute
from django.utils import timezone
from django.db.models import F, DecimalField
from django.contrib import messages
from django.forms.models import modelformset_factory
from django.contrib.auth import logout
from django.views.generic.edit import UpdateView


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








# start control panel


def control_home(request):
    context = {
        'title': 'لوحة التحكم'
    }

    return render(request, 'control/control-home.html', context)




def control_list_product(request):

    products = Product.objects.all()

    return render(request, 'control/control-list.html', {'products': products})
    



def control_add_product(request):

    ImageFormSet = modelformset_factory(Image, form=ImageForm, extra=3)
    AttributeFormSet = modelformset_factory(ProductAttribute, form=ProductAttributeForm)

    if request.method == 'POST':
        productForm = ProductForm(request.POST or None, request.FILES or None)
        formset = ImageFormSet(request.POST or None, request.FILES or None)
        
        if productForm.is_valid() and formset.is_valid():
            productForm.save()
            for form in formset.cleaned_data:
                #this helps to not crash if the user   
                #do not upload all the photos
                if form:
                    product_instance = productForm.save()
                    image = form['image']
                    photo = Image(product=product_instance, image=image)
                    photo.save()
            messages.success(request,
                             "Yeeew, check it out on the home page!")
            
            return HttpResponseRedirect("/")


        else:
            return HttpResponse('postForm.errors, formset.errors')

    else:
        productForm = ProductForm()
        formset = ImageFormSet(queryset=Image.objects.none())
        

    context = {
        'prodectForm': productForm,
        'formset': formset,
    }
    return render(request, 'control/control-new-product.html', context)


class ProductUpdate(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'control/control-edit-product.html'

    def get_object(self):
        id_ = self.kwargs.get('product_id')
        return get_object_or_404(Product, id=id_)


def control_add_product_attribute(request, product_id):
    product = get_object_or_404(Product,pk=product_id)
    AttributeFormSet = modelformset_factory(ProductAttribute, form=ProductAttributeForm)

    if request.method == 'POST':
        formset = AttributeFormSet(request.POST, queryset=ProductAttribute.objects.filter(product__id=product.id))
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.product_id = product.id
                instance.save()

            return redirect('add_product_attribute', product_id=product.id )
        else:
            return HttpResponse('erroe')
    
    else:

        formset = AttributeFormSet(queryset=ProductAttribute.objects.filter(product__id=product.id))
    context = {

        'formsetattr': formset,

    }
    return render(request, 'control/control-new-product-attribute.html', context)

def control_add_product_discount(request, product_id):
    product = get_object_or_404(Product,pk=product_id)
    if request.method == 'POST':
        form = ProductDiscountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ProductDiscountForm(initial = {'product': product_id})
    context = {

        'product':product,
        'form': form,
    }
    return render(request, 'control/control-new-product-discount.html', context)

def control_delete_product(request, product_id):

    product = get_object_or_404(Product,pk=product_id)
    product.delete()
    return redirect('/')
    



def logout_view(request):
    logout(request)
    return redirect('/')


# end control panel




def product_detail(request, product_id):
    product = get_object_or_404(Product,pk=product_id)
    context = {
        'product': product
    }
    return render(request, 'store/product-detail.html', context)

