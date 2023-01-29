from django.db import models

# Models
# {"cart_value": 790, "delivery_distance": 2235, "number_of_items": 4, "time": "2021-10-12T13:00:00Z"}
class Delivery(models.Model):
    cart_value = models.IntegerField()
    delivery_distance = models.IntegerField()
    number_of_items = models.IntegerField()
    time = models.CharField(max_length=21)

    class Meta:
        verbose_name = 'Delivery'
        verbose_name_plural = 'Deliveries'