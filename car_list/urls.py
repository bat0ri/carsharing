from django.urls import path
from .views import car_list, offer_detail, main_page, cart_view, add_to_cart, remove_from_cart, increase_quantity, decrease_quantity, payment_page, add_page, transport_delete
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', main_page, name='main'),
    path('list/<slug:transport_type>/', car_list, name='offers'),
    path('offers/<int:offer_id>/', offer_detail, name='offer'),
    path('cart/', cart_view, name='cart'),
    path('cart/add/<int:transport_id>/', add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:transport_id>/', remove_from_cart, name='remove_from_cart'),
    path('cart/increase_quantity/<int:item_id>/', increase_quantity, name='increase_quantity'),
    path('cart/decrease_quantity/<int:item_id>/', decrease_quantity, name='decrease_quantity'),
    path('payment/', payment_page, name='payment'),
    path('add/', add_page, name='add'),
    path('delete/<int:offer_id>/', transport_delete, name='delete')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
