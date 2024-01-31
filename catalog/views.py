from django.shortcuts import render


def index(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'catalog/index.html', context)


def catalog(request):
    context = {
        'title': 'Каталог',
    }
    
    return render(request, 'catalog/catalog.html', context)