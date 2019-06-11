from django.db import models

# Create your models here.
class Prodect(models.Model):

    title = models.CharField(max_length=150)
    prise = models.IntegerField(default=170)
    img = models.ImageField(upload_to = 'images')

    def __str__(self):
        return self.title

