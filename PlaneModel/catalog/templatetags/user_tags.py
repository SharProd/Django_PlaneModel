from django import template
from catalog.models import ImageItem,CatalogItem,Category,BasketProduct


register = template.Library()

@register.simple_tag()
def get_category():
    return Category.objects.all()


@register.simple_tag()
def main_image_in_product():
    images_all = ImageItem.objects.all()
    images_item_id = []
    images_only = []
    for i in images_all:
        if i.item_id in images_item_id:
            pass
        else:
            images_only.append(i)
            images_item_id.append(i.item_id)
    return images_only

@register.simple_tag()
def id_product():
    id_set = list(map(lambda item: item.id, CatalogItem.objects.all()))
    return id_set

@register.simple_tag()
def len_baskets(user):
    basket = BasketProduct.objects.filter(user_id = user.id)
    return len(basket)

@register.simple_tag()
def basket(user):
    basket = BasketProduct.objects.filter(user_id = user.id)
    product_id_in_basket = list(map(lambda x:x.product_id,basket))
    product_in_basket = list( i for i in CatalogItem.objects.all() if i.id in product_id_in_basket)
    return product_in_basket