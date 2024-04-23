from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login
from django.contrib import messages

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=email, password=password)

        if user is not None:
            # User authentication successful, log them in
            login(request, user)
            return redirect('inventory') 
        else:
            # User authentication failed, display an error message
            messages.error(request, 'Invalid email or password. Please try again.')

    # Render the login page
    return render(request, 'login.html')