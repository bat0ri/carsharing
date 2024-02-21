from django.urls import path

from catalog.views import busket_add, busket_remove, CatalogView

app_name = 'catalog/'

urlpatterns = [

    path('', CatalogView.as_view(), name='index'),
    path('category/<int:category_id>', CatalogView.as_view(), name='category'),
    path('buskets/add/<int:transport_id>',busket_add, name='busket_add'),
    path('buskets/remove/<int:busket_id>',busket_remove, name='busket_remove')

]

