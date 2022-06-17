from django.views.generic import ListView
# from .models import Category
from .models import Category


class CatalogListView(ListView):

    model = Category
    template_name = "catalog/index.html"
    context_object_name = "category"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'main'
        return context

    # def get_queryset(self):
    #     pass