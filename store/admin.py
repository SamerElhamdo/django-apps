from django.contrib import admin
from store.models import Product, ProductAttribute, Order

# Register your models here.
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(ProductAttribute)

