from django.urls import path
from .views import *

urlpatterns = [
    path('',CatalogListView.as_view(),name = 'catalog'),
    path('<str:slug>_<int:pk>/',ItemByCatalog.as_view(),name = 'category'),
    path('<int:pk>/', Item.as_view(),name = 'item_page')
]

