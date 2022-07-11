from django import forms
from .models import CatalogItem,ImageItem


class ProductForm(forms.ModelForm):

    class Meta:
        model = CatalogItem
        fields = ['title','info','price','weight','is_published','category']


        widgets = {'title':forms.TextInput(attrs={'class':'form-control',"placeholder": "Название"}),
                   'info':forms.Textarea(attrs={'class':'form-control'}),
                   }


class ImageProductForm(forms.ModelForm):

    class Meta:
        model = ImageItem
        fields = ('image',)






