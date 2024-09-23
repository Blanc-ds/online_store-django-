from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {
        'title': 'Home',
        'content': 'Shop\'s main page'
    }
    return render(request, 'main/index.html', context=context)

def about(request):
    return HttpResponse('About us')
