from django.shortcuts import render

# Create your views here.
def catalog(request):
    # context = {
    #     'title': 'Catalog',
    #     'content': 'Our products'
    # }
    return render(request, 'goods/catalog.html')

def product(request):
    # context = {
    #     'title': 'Home - About us',
    #     'content': 'The page about us',
    #     'text_on_page': 'Some usefull information about us',
    # }

    return render(request, 'goods/product.html')

