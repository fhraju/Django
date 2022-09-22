from django.urls import path

from .views import products_detail, category_details

urlpatterns = [
    path('<slug:slug>/', category_details, name='category_details'),
    path('<slug:category_slug>/<slug:slug>/', products_detail, name='products_detail'),
]