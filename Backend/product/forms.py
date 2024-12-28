from django import forms
from .models import Product
# from .models import Product

class ProductForm(forms.Form):
    name = forms.CharField(error_messages={"required":"Ce champs ne doit pas etre vide"},required=True)
    price = forms.IntegerField(label="Product Price",)
    description = forms.CharField(max_length=200)

class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
    
    class Media:
        css = {
            'all': ('css/style.css',)
        }
        # js = ('js/script.js',)

    