from django.db import models
from django.urls import reverse

# Create your models here.







class Product(models.Model):

    title = models.CharField(max_length=150)
    price = models.IntegerField(default=170)

    percentage = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    img = models.ImageField(upload_to = 'images', blank=True, null=True)

    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('edit_product', kwargs={'product_id': self.pk})

"""     def save(self, *args, **kwargs):
        if self.discount:
                
            decimal = self.percentage / 100

            self.new_price = self.price - (self.price * decimal)

            super().save(*args, **kwargs)  

        super().save(*args, **kwargs)   """
    








class ProductAttributeManager(models.Manager):
    def colors(self):
        return super(ProductAttributeManager, self).filter(category='color')

    def sizes(self):
        return super(ProductAttributeManager, self).filter(category='size')


    

VAR_CATEGORIES = [
    ('اللون', 'اللون'),
    ('القياس', 'القياس'),

]

class ProductAttribute(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    category = models.CharField(max_length=150, choices=VAR_CATEGORIES, default='size')
    attr = models.CharField(max_length=150)

    objects = ProductAttributeManager()

    def __str__(self):
        return self.attr


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=None)
    image = models.ImageField(upload_to='product/images')

    def __str__(self):
        return self.product.title + ' صورة '


class Discount(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    percentage = models.DecimalField(max_digits=19, decimal_places=2)
    date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.title



class Order(models.Model):

    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    full_name = models.CharField(max_length=150)
    phonenumber = models.CharField(max_length=10)
    accept = models.BooleanField(default=False)
    color = models.CharField(max_length=150)
    size = models.CharField(max_length=150)
    

    def __str__(self):
        return self.full_name + ' ' + self.product.title