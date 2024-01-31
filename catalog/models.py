from django.db import models



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