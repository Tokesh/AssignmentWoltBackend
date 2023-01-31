from unittest import TestCase
from api.models import Delivery
from api.business_logic import calculateDeliveryFee

class LogicTestCase(TestCase):

    def test_cart(self):
        # Testing cart less < 10 euro
        delivery = Delivery(cart_value=695, delivery_distance=0, number_of_items=4, time="2021-10-12T13:00:00Z")
        result = calculateDeliveryFee(delivery)
        self.assertEqual(505, result)
    def test_distance1(self):
        # Testing distance = 501 m, that mean less than 1 km = 2 euro
        delivery = Delivery(cart_value=1000, delivery_distance=501, number_of_items=4, time="2021-10-12T13:00:00Z")
        result = calculateDeliveryFee(delivery)
        self.assertEqual(200, result)
    def test_distance2(self):
        # Testing distance = 1501, 2€ base fee + 1€ for the first 500 m + 1€ for the second 500 m => 4€
        delivery = Delivery(cart_value=1000, delivery_distance=1501, number_of_items=4, time="2021-10-12T13:00:00Z")
        result = calculateDeliveryFee(delivery)
        self.assertEqual(400, result)
    def test_items_count(self):
        # Testing items count (Delivery distance first 1km = 2 euros and 2 items = 0.5*2, total = 3 euros)
        delivery = Delivery(cart_value=1000, delivery_distance=0, number_of_items=6, time="2021-10-12T13:00:00Z")
        result = calculateDeliveryFee(delivery)
        self.assertEqual(300, result)

    def test_friday_rush(self):
        # Testing Friday Rush( first 1km = 2 euros, multiply 1.2 for friday rush)
        delivery = Delivery(cart_value=1000, delivery_distance=0, number_of_items=4, time="2021-10-15T16:00:00Z")
        result = calculateDeliveryFee(delivery)
        self.assertEqual(240, result)

    def test_max_surcharge(self):
        # Testing max limit
        delivery = Delivery(cart_value=1000, delivery_distance=0, number_of_items=1001, time="2021-10-12T13:00:00Z")
        result = calculateDeliveryFee(delivery)
        self.assertEqual(1500, result)
    def test_delivery_free(self):
        # Testing free delivery for cart_value >= 100 euros
        delivery = Delivery(cart_value=10000, delivery_distance=0, number_of_items=6, time="2021-10-12T13:00:00Z")
        result = calculateDeliveryFee(delivery)
        self.assertEqual(0, result)

    def test_custom_delivery(self):
        # AVG user delivery checking
        delivery = Delivery(cart_value=2200, delivery_distance=1680, number_of_items=6, time="2021-10-12T13:00:00Z")
        result = calculateDeliveryFee(delivery)
        self.assertEqual(500, result)