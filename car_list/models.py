from django.db import models
from django.contrib.auth.models import User
from django.db.models import ImageField


class Transport(models.Model):
    type =  models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.IntegerField()            # вместительность
    image = ImageField(upload_to='images/', null=True, blank=True)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    arenda = models.CharField(max_length=50, null=True)
    is_booked = models.BooleanField(default=False)


class TransportImage(models.Model):
    transport = models.ForeignKey(Transport, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='transport_images/', blank=True, null=True)


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cart - {self.user.username}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    transport = models.ForeignKey(Transport, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    def __str__(self):
        return f"CartItem - {self.transport.name} (Quantity: {self.quantity})"


class Booking(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Booking - {self.user.username}"


class BookingItem(models.Model):
    booking = models.ForeignKey(Booking, related_name='items', on_delete=models.CASCADE)
    transport = models.ForeignKey(Transport, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"CartItem - {self.transport.name} (Quantity: {self.quantity})"