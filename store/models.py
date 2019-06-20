from django.db import models

# Create your models here.







class Product(models.Model):

    title = models.CharField(max_length=150)
    price = models.IntegerField(default=170)
    discount = models.BooleanField(default=True)
    percentage = models.DecimalField(max_digits=19, decimal_places=2)
    new_price = models.IntegerField(blank=True)
    img = models.ImageField(upload_to = 'images')

    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):

        decimal = self.percentage / 100

        self.new_price = self.price - (self.price * decimal)

        super().save(*args, **kwargs)  # Call the "real" save() method.



class ProductAttributeManager(models.Manager):
    def colors(self):
        return super(ProductAttributeManager, self).filter(category='color')

    def sizes(self):
        return super(ProductAttributeManager, self).filter(category='size')


    

VAR_CATEGORIES = [
    ('color', 'color'),
    ('size', 'size'),

]

class ProductAttribute(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    category = models.CharField(max_length=150, choices=VAR_CATEGORIES, default='size')
    attr = models.CharField(max_length=150)

    objects = ProductAttributeManager()

    def __str__(self):
        return self.attr





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