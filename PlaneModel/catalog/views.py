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
        return context


class ItemByCatalog(CatalogListView):
    # model = CatalogItem
    # template_name = "catalog/index.html"
    # context_object_name = "item_catalog"

    # def get_queryset(self):
    #     return CatalogItem.objects.filter(slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ItemByCatalog, self).get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug = self.kwargs['slug'])
        context['product'] = CatalogItem.objects.all()
        context['images'] = ImageItem.objects.all()
        return context

