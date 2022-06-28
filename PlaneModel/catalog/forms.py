from django import forms
from .models import Category,CatalogItem


class CreateProduct(forms.ModelForm):
    # title = forms.CharField(max_length=50,label='название')
    # info = forms.CharField(max_length=200,label='инф. о продукте')
    # price = forms.FloatField(label='цена')
    # is_published = forms.BooleanField(required=False)
    # weight = forms.FloatField(label='вес')
    # category = forms.ModelChoiceField(empty_label='none',queryset=Category.objects.all(),label='категория')

    class Meta:
        model = CatalogItem
        fields = '__all__'
