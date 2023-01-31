from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from api.models import Delivery
from api.serializers.serializer import deliverySerializer
from datetime import datetime
from api.business_logic import calculateDeliveryFee

@api_view(['GET'])
def getDeliveryFeeCents(request):
    if request.method == 'GET':
        serializer = deliverySerializer(data=request.data)
        if serializer.is_valid():
            delivery = Delivery(**dict(serializer.data))
            delivery_fee = calculateDeliveryFee(delivery)
            return Response({'delivery_fee': delivery_fee}, status=status.HTTP_200_OK)

        return Response(status.HTTP_400_BAD_REQUEST)
