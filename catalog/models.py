from django.db import models
from users.models import User


class TransportCategory(models.Model):
    
    name = models.CharField(max_length=80)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Transport(models.Model):

    name = models.CharField(max_length=80)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_ready = models.BooleanField(default=True)
    image = models.ImageField(upload_to='transport_images')
    category = models.ForeignKey(to=TransportCategory, on_delete=models.CASCADE)


    def __str__(self):
        return f"Транспорт: {self.name} ||--|| Тип: {self.category.name}"


class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum() for basket in self)

    def total_quantity(self):
        return sum(basket.quantity for basket in self)



class Busket(models.Model):

    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    transport = models.ForeignKey(to=Transport, on_delete=models.CASCADE)
    minutes = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    objects = BasketQuerySet.as_manager()

    class Meta:
        verbose_name = ("Busket")
        verbose_name_plural = ("Buskets")

    def __str__(self):
        return f'Корзина для {self.user.email}, Продукт: {self.transport.name}'

    def get_absolute_url(self):
        return reverse("Busket_detail", kwargs={"pk": self.pk})

    def sum(self):
        return self.transport.price * self.minutes
