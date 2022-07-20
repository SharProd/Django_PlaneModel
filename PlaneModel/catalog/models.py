import datetime

from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User


class CatalogItem(models.Model):
    title = models.CharField(max_length=50,verbose_name='title')
    info = models.CharField(max_length=200,null=True,blank = True)
    slug = models.SlugField()
    price = models.FloatField(verbose_name="price")
    is_published = models.BooleanField(default=True,verbose_name="есть в наличии")
    weight = models.FloatField(default=0.0, verbose_name="weight")
    publication_date = models.DateTimeField(auto_now_add=True, verbose_name='date of publication')
    edit_date = models.DateTimeField(auto_now_add=True, verbose_name="date of edit product")
    category = TreeForeignKey('Category', on_delete=models.PROTECT,null=True, related_name='posts', verbose_name='category')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('item_page',kwargs={'item_slug':self.slug,'pk':self.pk})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return  super(CatalogItem, self).save(*args, **kwargs)


    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'


class Category(MPTTModel):
    title = models.CharField(max_length=50, unique=True, verbose_name='name')
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children',db_index=True, verbose_name='Parent ')
    slug = models.SlugField()

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        unique_together = [['parent', 'slug']]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title


class ImageItem(models.Model):
    image = models.ImageField(upload_to='image/%Y/%m/%d/',verbose_name='image')
    item = models.ForeignKey(CatalogItem,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.item_id)

    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'images'


class BasketProduct(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(CatalogItem,on_delete=models.CASCADE)

    def __str__(self):
        return str(f"{self.user} {self.product}")

    class Meta:
        verbose_name = 'basket'
        verbose_name_plural = 'baskets'
