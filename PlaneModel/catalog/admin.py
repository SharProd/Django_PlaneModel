from django.contrib import admin
from .models import CatalogItem, Category, ImageItem
from django_mptt_admin.admin import DjangoMpttAdmin

class ImageItemAdmin(admin.ModelAdmin):
    list_display = ('item_id',)

class CatalogItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(CatalogItem, CatalogItemAdmin)


class CategoryAdmin(DjangoMpttAdmin):
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ('title',)
    list_filter = ('title',)

admin.site.register(ImageItem, ImageItemAdmin)
admin.site.register(Category, CategoryAdmin)