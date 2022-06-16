from django.urls import path

from catalog.views import CatalogListView

urlpatterns = [
    path('catalog/',CatalogListView.as_view()),
]
