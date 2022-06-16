from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey



class CatalogItem(models.Model):
    title = models.CharField(max_length=50,verbose_name='назавание')
    item_info = models.CharField(max_length=200,null=True)
    slug = models.SlugField()
    price = models.IntegerField(verbose_name="цена")
    is_published = models.BooleanField(default=True,verbose_name="есть в наличии")
    item_weight = models.IntegerField(verbose_name="вес")
    item_image = models.ImageField(upload_to='image/%Y/%m/%d/',verbose_name='изображение')
    category = TreeForeignKey('Category', on_delete=models.PROTECT,null=True, related_name='posts', verbose_name='Категория')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'


class Category(MPTTModel):
    title = models.CharField(max_length=50, unique=True, verbose_name='Название')
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children',
                            db_index=True, verbose_name='Родительская категория')
    slug = models.SlugField()

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        unique_together = [['parent', 'slug']]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('post-by-category', args=[str(self.slug)])

    def __str__(self):
        return self.title