from django.shortcuts import render, HttpResponseRedirect
from catalog.models import Transport, TransportCategory, Busket


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

def busket_add(request, transport_id):
    transport = Transport.objects.get(id=transport_id)
    buskets = Busket.objects.filter(user=request.user, transport=transport)

    if not buskets.exists():
        Busket.objects.create(transport=transport, user=request.user, minutes=10)
    else:
        busket = buskets.first()
        busket.minutes += 10
        busket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def busket_remove(request, busket_id):
    busket = Busket.objects.get(id=busket_id)
    busket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
