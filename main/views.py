from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {
        'title': 'Home',
        'content': 'Shop\'s main page'
    }
    return render(request, 'main/index.html', context=context)

def about(request):
    context = {
        'title': 'Home - About us',
        'content': 'The page about us',
        'text_on_page': 'Some usefull information about us'
    }
    return render(request, 'main/about.html', context=context)

def contacts(request):
    context = {
        'title': 'Home - Contacts',
        'content': 'The page about our contacts',
        'text_on_page': 'Some usefull information about contacts'
    }
    return render(request, 'main/contacts.html', context=context)

def payment(request):
    context = {
        'title': 'Home - Payment and delivery',
        'content': 'The page about payment methods and delivery',
        'text_on_page': 'Some usefull information payment'
    }
    return render(request, 'main/payment.html', context=context)

