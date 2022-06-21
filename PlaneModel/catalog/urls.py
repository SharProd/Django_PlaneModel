from django.urls import path
from .views import *

urlpatterns = [
    path('',CatalogListView.as_view(),name = 'catalog'),
    path('<str:slug>_<int:id>/',ItemByCatalog.as_view(),name = 'category'),
]

