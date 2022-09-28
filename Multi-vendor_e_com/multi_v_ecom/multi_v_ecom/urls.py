from django.contrib import admin
from django.urls import path, include
#for static files
from django.conf import settings
from django.conf.urls.static import static

from core.views import frontpage, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about, name='about'),
    path('', include('usersprofile.urls')),
    path('', include('products_store.urls')),
    path('', frontpage, name='frontpage'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
