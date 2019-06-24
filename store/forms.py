from django import forms
from .models import Product, ProductAttribute, Image, Order, Discount
from django.utils.translation import gettext_lazy as _

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('title', 'price', 'img', )


        labels = {
            'title': _('أسم المنتج'),
            'price': _(' سعر المنتج'),
            'img': _('صورة المنتج'),

            
            
        }
        widgets = {

            'img': forms.FileInput(attrs={'style':'display: none;'}),
            
        }




class ProductDiscountForm(forms.ModelForm):
    
    class Meta:
        model = Discount
        fields = ('product', 'title', 'percentage', 'date',)

        widgets = {

            'product': forms.HiddenInput(),
 
        }

        labels = {
            'title': _('أسم الحسم'),
            'percentage': _('قيمة الحسم'),
            'date': _('تاريخ إنتهاء الحسم'),

        }

        help_texts = {
            'percentage': _('نسبة مئوية'),
            
        }

class ProductAttributeForm(forms.ModelForm):
    
    class Meta:
        model = ProductAttribute
        fields = ('product', 'category', 'attr',)

        widgets = {
            'product': forms.HiddenInput(),

            
        }


        labels = {
            'category': _(' النوع'),
            'attr': _(' القيمة'),
            


        }

        help_texts = {
            'category': _(' لون أو قياس'),
            'attr': _(' قيمة اللون أو القياس '),
            
            
        }

    def __init__(self, *args, **kwargs):
        super(ProductAttributeForm, self).__init__(*args, **kwargs)
        self.fields['product'].required = False

        


class ImageForm(forms.ModelForm):   
    class Meta:
        model = Image
        fields = ('image', )


        labels = {
            'image': _('أرفع الصورة '),


        }



class OrderForm(forms.ModelForm):
    
    class Meta:
        model = Order
        fields = ('product', 'quantity', 'full_name', 'phonenumber', 'color', 'size')


        widgets = {
            'quantity': forms.TextInput(attrs={'maxlength':'100'}),
            'product': forms.HiddenInput(),
            'color': forms.HiddenInput(),
            'size': forms.HiddenInput(),
            
        }
        labels = {
            'quantity': _('الكمية'),
            'full_name': _('الأسم الكامل'),
            'phonenumber': _('رقم الهاتف'),
            
        }
        help_texts = {
            'phonenumber': _('أدخل رقم هاتف صحيح للتواصل معكم'),
        }

