from django.contrib import admin
from django.urls import path, include

from core.views import frontpage, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about, name='about'),
    path('', include('products_store.urls')),
    path('', frontpage, name='frontpage'),
]