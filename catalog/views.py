from django.shortcuts import render
from catalog.models import Transport, TransportCategory


def index(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'catalog/index.html', context)


def catalog(request):
    context = {
        'title': 'Каталог',
        'transports': Transport.objects.all(),
        'categories': TransportCategory.objects.all()
    }
    
    return render(request, 'catalog/catalog.html', context)