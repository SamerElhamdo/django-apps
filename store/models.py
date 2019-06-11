from django.db import models

# Create your models here.







class Prodect(models.Model):

    title = models.CharField(max_length=150)
    price = models.IntegerField(default=170)
    img = models.ImageField(upload_to = 'images')

    def __str__(self):
        return self.title


class Discount(models.Model):
    discount_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Prodect, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    percentage = models.DecimalField(max_digits=19, decimal_places=2)
    expire_date = models.DateField()


    def __str__(self):
        return self.title