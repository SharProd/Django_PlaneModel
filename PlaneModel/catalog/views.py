from django.shortcuts import render
from django.views.generic import ListView
from .models import *



# def catalog_view(request):
#     category = Category.objects.all()
#     product = CatalogItem.objects.all()
#     images = ImageItem.objects.all()
#     data = {'category': category,
#             'product': product,
#             'images': images
#             }
#     return render(request,'catalog/index.html',context=data)
#
# def select_category(request,slug,id):
#     category = Category.objects.all()
#     product = CatalogItem.objects.all()
#
#     data = {'category': category,
#             'product': product,
#             }
#     return render(request, 'catalog/index.html', context=data)
class CatalogListView(ListView):

    model = Category
    template_name = "catalog/index.html"
    context_object_name = "category"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Каталог'
        context['product'] = CatalogItem.objects.all()
        # context['images'] =ImageItem.objects.all()
        # print(len(context['images']))
        return context


class ItemByCatalog(ListView):
    model = CatalogItem
    template_name = "catalog/index.html"
    context_object_name = "product"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ItemByCatalog, self).get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug = self.kwargs['slug'])
        # context['images'] = ImageItem.objects.all()
        return context

    def get_queryset(self):
        return CatalogItem.objects.filter(category_id=self.kwargs['pk'])

def home_page(request):
    return render(request, 'catalog/home_page.html',context={'title':'Главная'})

class Item(ItemByCatalog):
    template_name = "catalog/item_page.html"
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ItemByCatalog, self).get_context_data(**kwargs)
        context['title'] = CatalogItem.objects.get(pk = self.kwargs['pk'])
        context['images'] = ImageItem.objects.filter(item_id = self.kwargs['pk'])
        return context

    def get_queryset(self):
        return CatalogItem.objects.get(pk=self.kwargs['pk'])
