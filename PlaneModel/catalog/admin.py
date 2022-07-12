from django.contrib import admin
from .models import CatalogItem, Category, ImageItem,BasketProduct
from django_mptt_admin.admin import DjangoMpttAdmin


class ImageItemAdmin(admin.ModelAdmin):
    list_display = ('item_id',)

class ProductImageInline(admin.StackedInline):
    model = ImageItem

class CatalogItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('id','title','category_id')
    list_display_links = ('id','title')
    inlines =[ProductImageInline]


class CategoryAdmin(DjangoMpttAdmin):
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ('title',)
    list_filter = ('title',)


class BasketProductAdmin(admin.ModelAdmin):
    list_display = ('user','product')


admin.site.register(BasketProduct, BasketProductAdmin)
admin.site.register(CatalogItem, CatalogItemAdmin)
admin.site.register(ImageItem, ImageItemAdmin)
admin.site.register(Category, CategoryAdmin)