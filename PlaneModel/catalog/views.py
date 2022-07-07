from django.shortcuts import render,redirect
from django.views.generic import ListView
from .models import *
from .forms import ProductForm,ImageProductForm
from .models import ImageItem
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages


class CatalogListView(ListView):
    model = CatalogItem
    template_name = "catalog/index.html"
    context_object_name = "product"
    ordering = ['-publication_date']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Каталог'
        return context


class ItemByCatalog(ListView):
    model = CatalogItem
    template_name = "catalog/index.html"
    context_object_name = "product"
    ordering = ['-publication_date']


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(id = self.kwargs['pk'])
        return context

    def get_queryset(self):
        return CatalogItem.objects.filter(category_id=self.kwargs['pk'])

def home_page(request):
    context = {'title':'Главная'}
    return render(request, 'catalog/home_page.html',context=context)


#создание запроса на данные для страницы товара
class Item(ItemByCatalog):
    template_name = "catalog/item_page.html"
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ItemByCatalog, self).get_context_data(**kwargs)
        context['title'] = CatalogItem.objects.get(pk = self.kwargs['pk'])
        context['images'] = ImageItem.objects.filter(item_id= self.kwargs['pk'])
        images = []
        # создание списка с url изображений вместо списка обьектовб,создание единичного элемента Главная фотография
        for i in context['images']:
            images.append(i.image)
        if images:
            context['main_image'] = images[0]
            context['other_image'] = images[1:]
        return context

    def get_queryset(self):
        return CatalogItem.objects.get(pk=self.kwargs['pk'])


class ItemInMainCategory(ListView):
    model = CatalogItem
    template_name = "catalog/index.html"
    context_object_name = "product"
    ordering = ['-publication_date']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        return context

    def get_queryset(self):
        return CatalogItem.objects.filter(category__tree_id=self.kwargs['tree_id'])


@login_required
def add_product(request):
    ImageFormSet = modelformset_factory(ImageItem,
                                        form=ImageProductForm, extra=3)
    if request.method == 'POST':

        productForm = ProductForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=ImageItem.objects.none())


        if productForm.is_valid() and formset.is_valid():
            product_form = productForm.save(commit=False)
            product_form.user = request.user
            product_form.save()
            for form in formset.cleaned_data:
                if form:
                    image = form['image']
                    print(f'form["image"] - {image}')
                    print(f'form - {form}')
                else:
                    image = 'static/no_photo.png'
                photo = ImageItem(item_id=product_form.pk, image=image)
                photo.save()
                messages.success(request,
                                 "Yeeew, check it out on the home page!")
                return redirect("catalog")

            messages.success(request,
                             "Yeeew, check it out on the home page!")
            return redirect("catalog")
        else:
            print(productForm.errors, formset.errors)
    else:
        product_form = ProductForm()
        formset = ImageFormSet(queryset=ImageItem.objects.none())
    return render(request, 'catalog/add_product.html',
                  {'product_form': product_form, 'formset': formset})