from django.shortcuts import render, HttpResponseRedirect
from catalog.models import Transport, TransportCategory, Busket
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required


class IndexView(TemplateView):
    template_name = 'catalog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Home' 
        return context


class CatalogView(ListView):
    model = Transport
    template_name = 'catalog/catalog.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category__id=category_id) if category_id else queryset

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Каталог' 
        context['categories'] = TransportCategory.objects.all()
        return context


#def catalog(request, category_id=None):
#    transports = Transport.objects.filter(category__id=category_id) if category_id else Transport.objects.all()
#    context = {
#        'title': 'Каталог',
#        'transports': transports,
#        'categories': TransportCategory.objects.all()
#    }
    
#    return render(request, 'catalog/catalog.html', context)


@login_required()
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


@login_required
def busket_remove(request, busket_id):
    busket = Busket.objects.get(id=busket_id)
    busket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
