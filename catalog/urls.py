from django.urls import path

from catalog.views import catalog, busket_add, busket_remove

app_name = 'catalog/'

urlpatterns = [

    path('', catalog, name='index'),
    path('buskets/add/<int:transport_id>',busket_add, name='busket_add'),
    path('buskets/remove/<int:busket_id>',busket_remove, name='busket_remove')

]

