from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import vendor_detail, signup, my_account

urlpatterns = [
    path('myaccount/', my_account, name='my_account'),
    path('login/', LoginView.as_view(template_name='usersprofile/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', signup, name='signup'),
    path('vendors/<int:pk>/', vendor_detail, name='vendor_detail'),
]
