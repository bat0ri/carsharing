from django.contrib import admin
from .models import Transport, TransportImage, BookingItem, CartItem

admin.site.register(Transport)
admin.site.register(CartItem)
admin.site.register(BookingItem)