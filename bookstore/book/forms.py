from pyexpat import model
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        models = User
        fields = ['username', 'password']

class CreateCustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__' # form for all without user
        exclude = ['user']

class CreateBookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

