from django.db import models

class Delivery(models.Model):
    cart_value = models.IntegerField()
    delivery_distance = models.IntegerField()
    number_of_items = models.IntegerField()
    time = models.CharField(max_length=21)

    class Meta:
        verbose_name = 'Delivery'
        verbose_name_plural = 'Deliveries'