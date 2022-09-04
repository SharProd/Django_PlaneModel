from django.urls import path,include
from .views import CatalogListView,Item,ItemByCatalog,ItemInMainCategory,add_product,SearchProduct
from rest_framework import routers
from .endpoints import CatItemVewSet,CategoryViewSet

router = routers.DefaultRouter()
router.register(r'items',CatItemVewSet)
router.register(r'category',CategoryViewSet)

urlpatterns = [
    path('',CatalogListView.as_view(),name = 'catalog'),
    path('<slug:slug>_<int:tree_id>/<int:pk>/',ItemByCatalog.as_view(),name = 'category'),
    path('<slug:slug>_<int:tree_id>/',ItemInMainCategory.as_view(),name = 'main_category'),
    path('<slug:item_slug>-<int:pk>/', Item.as_view(),name = 'item_page'),
    path('add_product/',add_product,name = 'add_product'),
    path('search/',SearchProduct.as_view(),name = 'search_product'),
    path('api/',include(router.urls)),
]

