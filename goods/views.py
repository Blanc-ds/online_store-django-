from django.shortcuts import render

from goods.models import Products

# Create your views here.
def catalog(request):
    goods = Products.objects.all()

    context = {
        'title': 'Catalog',
        'goods': goods,
    }
    return render(request, 'goods/catalog.html', context=context)

def product(request):
    # context = {
    #     'title': 'Home - About us',
    #     'content': 'The page about us',
    #     'text_on_page': 'Some usefull information about us',
    # }

    return render(request, 'goods/product.html')

