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

    model = CatalogItem
    template_name = "catalog/index.html"
    context_object_name = "product"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Каталог'
        return context


class ItemByCatalog(ListView):
    model = CatalogItem
    template_name = "catalog/index.html"
    context_object_name = "product"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['title'] = Category.objects.get(id__pk = self.kwargs['pk'])
        return context

    def get_queryset(self):
        return CatalogItem.objects.filter(category_id=self.kwargs['pk'])

def home_page(request):
    return render(request, 'catalog/home_page.html',context={'title':'Главная'})


#создание запроса на данные для страницы товара
class Item(ItemByCatalog):
    template_name = "catalog/item_page.html"
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):

        context = super(ItemByCatalog, self).get_context_data(**kwargs)
        # context['title'] = CatalogItem.objects.get(pk = self.kwargs['pk'])
        context['images'] = ImageItem.objects.filter(item_id= self.kwargs['pk'])
        images = []
        # создание списка с url изображений вместо списка обьектовб,создание единичного элемента Главная фотография
        for i in context['images']:
            images.append(i.image)
        context['main_image'] = images[0]
        context['other_image'] = images[1:]
        return context

    def get_queryset(self):
        return CatalogItem.objects.get(pk=self.kwargs['pk'])






class ItemInMainCategory(ListView):
    model = CatalogItem
    template_name = "catalog/index.html"
    context_object_name = "product"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        return context

    def get_queryset(self):
        return CatalogItem.objects.filter(category__tree_id=self.kwargs['tree_id'])