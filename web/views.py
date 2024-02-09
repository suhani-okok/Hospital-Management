# web/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def index(request):
    if request.method == 'POST':
        # Handle sign up form submission
        # Perform sign-up logic
        return redirect('login')  # Redirect to login page after successful sign-up
    return render(request, 'web/index.html')

def login(request):
    if request.method == 'POST':
        # Handle login form submission
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the home page after successful login

    return render(request, 'web/login.html')

def home(request):
    # Handle home page logic
    return render(request, 'web/home.html')
