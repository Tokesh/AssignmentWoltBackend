from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from api.models import Delivery
from api.serializers.serializer import deliverySerializer
from datetime import datetime


@api_view(['GET'])
def getDeliveryFeeCents(request):
    if request.method == 'GET':
        serializer = deliverySerializer(data=request.data)
        if serializer.is_valid():
            delivery_fee = 0
            # We will calculate Delivery Fee in Euros and only in response we give our answer in Cents
            delivery = Delivery(**dict(serializer.data))
                
            # Cart value < 10 euros
            if delivery.cart_value < 1000:
                delivery_fee += (1000 - delivery.cart_value) / 100

            # Distance calculations
            if delivery.delivery_distance < 500:
                delivery_fee += 1
            elif delivery.delivery_distance:
                delivery_fee += delivery.delivery_distance / 500 + min(delivery.delivery_distance % 500, 1)

            # Number of Items calculations
            if delivery.number_of_items >= 5:
                delivery_fee += (delivery.number_of_items-4)*0.5
                if delivery.number_of_items > 12:
                    delivery_fee += 1.20

            # Checking for Friday Rush ( if day == Friday 15:00-19:00 )
            order_date = datetime.strptime(delivery.time, "%Y-%m-%dT%H:%M:%SZ")
            if 15 <= order_date.hour <= 17 and order_date.weekday() == 4:
                delivery_fee *= 1.2

            # Free delivery if cart value > 100 euros
            if delivery.cart_value >= 10000:
                delivery_fee = 0

            # Delivery Fee shouldn't be more than 15 Euros
            return Response({'delivery_fee': min(int(delivery_fee*100), 1500)}, status=status.HTTP_200_OK)

        return Response(status.HTTP_400_BAD_REQUEST)
