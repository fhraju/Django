from django import template

from products_store.models import Category

register = template.Library()

@register.inclusion_tag('core/menu.html')# this for menu outside templates
def menu():
    category = Category.objects.all()
    return {'categories':category}