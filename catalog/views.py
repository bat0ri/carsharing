from django.shortcuts import render, HttpResponseRedirect
from catalog.models import Transport, TransportCategory, Busket
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from common.views import CommonTitleMixin
from django.core.cache import cache


class IndexView(CommonTitleMixin, TemplateView):
    template_name = 'catalog/index.html'
    title = 'Home'


class CatalogView(CommonTitleMixin, ListView):
    model = Transport
    template_name = 'catalog/catalog.html'
    title = 'Каталог'

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category__id=category_id) if category_id else queryset

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        categries = cache.get('categories')
        if not categries:
            context['categories'] = TransportCategory.objects.all()
            cache.set('categories', context['categories'], 300)

        return context


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
