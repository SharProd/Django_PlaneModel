from django.urls import path
from .views import *

urlpatterns = [
    path('',CatalogListView.as_view()),
    path('<str:slug>_<int:id>/',ItemByCatalog.as_view())
]

