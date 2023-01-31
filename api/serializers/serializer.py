from rest_framework import serializers
from api.models import Delivery
class deliverySerializer(serializers.ModelSerializer):

    class Meta:
        model = Delivery
        fields = (
            'cart_value',
            'delivery_distance',
            'number_of_items',
            'time'
        )
