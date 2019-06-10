from django import forms
from .models import Prodect

class ProdectForm(forms.ModelForm):

    class Meta:
        model = Prodect
        fields = ('title', 'prise', 'img' )