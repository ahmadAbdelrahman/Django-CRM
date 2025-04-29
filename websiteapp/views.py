from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def index(request):

    # check to see if the user is logged in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        #Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have logged in!')
            return redirect('home')
        else:
            messages.success(request, 'Error')
            return redirect('home')
    else:
        return render(request, 'index.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, 'You have logged out!')
    return redirect('home')


def regestire_user(request):
    return render(request, 'register.html', {})