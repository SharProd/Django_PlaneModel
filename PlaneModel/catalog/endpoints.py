from .serializers import (CatItemSerializer,
                          CategorySerializer,
                          )
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .models import (CatalogItem,
                    Category,
                     )

class CatItemVewSet(ModelViewSet):
    serializer_class = CatItemSerializer
    queryset = CatalogItem.objects.all()
    permission_classes = [permissions.AllowAny]


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [permissions.AllowAny]