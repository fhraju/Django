from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password) # Must remove this print statement because it is a security flaw
        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {'error': "Invalid Username or Password"}
            return render(request, "accounts/login.html", context)
        login(request, user)
        return redirect('/admin')
    return render(request, "accounts/login.html", {})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect("/login/")
    return render(request, "accounts/logout.html", {})

def register_view(request):
    return render(request, "accounts/register.html", {})