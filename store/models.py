from django.db import models

# Create your models here.







class Prodect(models.Model):

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

    