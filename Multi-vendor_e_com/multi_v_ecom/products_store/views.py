from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from .models import Product, Category

def search(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))

    return render(request, 'products_store/search.html', {'query': query, 'products':products})

def category_details(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.all()
    return render(request, 'products_store/category_details.html', 
    {'categories': category, 'products':products})

# Products detail view
def products_detail(request, category_slug, slug):
    product = get_object_or_404(Product, slug = slug)
    return render(request, 'products_store/products_detail.html', {'product':product})
