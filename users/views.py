from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required

from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm



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
                messages.success(request, 'You logged in accaunt')

                if request.POST.get('next', None):
                    return HttpResponseRedirect(request.POST.get('next'))
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
            messages.success(request, f'{user.username} you succesfuly registrated and loged in')
            return HttpResponseRedirect(reverse('main:index'))


    else:
        form = UserRegistrationForm()

    context = {
        'title': 'Home - Registration',
        'form': form,
    }
    return render(request, 'users/registration.html', context=context)

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile has been successfuly updated')
            return HttpResponseRedirect(reverse('user:profile'))
        
    else:
        form = ProfileForm(instance=request.user)

    context = {
        'title': 'Home - Profile',
        'form': form,
    }
    return render(request, 'users/profile.html', context=context)

@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, 'You logged out')
    return redirect(reverse('main:index'))