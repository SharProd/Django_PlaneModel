from django.urls import path
from .views import CatalogListView,Item,ItemByCatalog,ItemInMainCategory

urlpatterns = [
    path('',CatalogListView.as_view(),name = 'catalog'),
    path('<slug:slug>_<int:tree_id>/<int:pk>/',ItemByCatalog.as_view(),name = 'category'),
    path('<slug:slug>_<int:tree_id>/',ItemInMainCategory.as_view(),name = 'main_category'),
    path('<int:pk>/', Item.as_view(),name = 'item_page')
]

