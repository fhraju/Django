from django.shortcuts import render

from products_store.models import Product

# We can use class based views here
def frontpage(request):
    products = Product.objects.all()[0:6]
    return render(request, 'core/frontpage.html', {'products':products})

def about(request):
    return render(request, 'core/about.html')
