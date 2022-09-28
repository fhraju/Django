from django.urls import path

from .views import products_detail, category_details, search

urlpatterns = [
    path('search/', search, name='search'),
    path('<slug:slug>/', category_details, name='category_details'),
    path('<slug:category_slug>/<slug:slug>/', products_detail, name='products_detail'),
]