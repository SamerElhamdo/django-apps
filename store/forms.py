from django import forms
from .models import Product, Order
from django.utils.translation import gettext_lazy as _

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('title', 'price', 'img', 'discount', 'percentage' )



class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('product', 'quantity', 'full_name', 'phonenumber', 'color', 'size')
        widgets = {

            'product': forms.HiddenInput(),
            'color': forms.HiddenInput(),
            'size': forms.HiddenInput(),
            
            
            'quantity': forms.NumberInput(),
        }
        labels = {
            'quantity': _('الكمية'),
            'full_name': _('الأسم الكامل'),
            'phonenumber': _('رقم الهاتف'),
            
        }
        help_texts = {
            'phonenumber': _('أدخل الرقم الهاتف الخاص بك سيتم ارسال كود تفعيل على رقمك لتأكيد الطلب'),
        }