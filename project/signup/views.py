from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def signup(request):
    if request.method == 'POST':
        # Retrieve signup form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Create a new user
        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = name
        user.save()

        # Authenticate and login the user
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a page after successful signup
            return redirect('login.html')  # Replace 'dashboard' with your desired URL

    return render(request, 'signup.html')

