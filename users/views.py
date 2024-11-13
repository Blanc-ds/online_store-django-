from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import auth

from users.forms import UserLoginForm, UserRegistrationForm



# Create your views here.

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))


    else:
        form = UserLoginForm()

    context = {
        'title': 'Home - Login',
        'form': form,
    }
    return render(request, 'users/login.html', context=context)

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main:index'))


    else:
        form = UserRegistrationForm()

    context = {
        'title': 'Home - Registration',
        'form': form,
    }
    return render(request, 'users/registration.html', context=context)

def profile(request):
    context = {
        'title': 'Home - Profile',
    }
    return render(request, 'users/profile.html', context=context)

def logout(request):
    auth.logout(request)
    return redirect(reverse('main:index'))