from django.urls import path,include
from .views import Item

urlpatterns = [
    path('<slug:slug>_<int:pk>/', Item.as_view(),name = 'item_page')
]
