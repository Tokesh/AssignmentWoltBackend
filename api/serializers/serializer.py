from rest_framework import serializers
from api.models import Delivery
# {"cart_value": 790, "delivery_distance": 2235, "number_of_items": 4, "time": "2021-10-12T13:00:00Z"}
class deliverySerializer(serializers.ModelSerializer):

    class Meta:
        model = Delivery
        fields = (
            'cart_value',
            'delivery_distance',
            'number_of_items',
            'time'
        )
