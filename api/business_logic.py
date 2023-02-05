from datetime import datetime



def calculateDeliveryFee(delivery):
    # We will calculate Delivery Fee in Euros and only in response we give our answer in Cents
    delivery_fee = 0
    # Free delivery if cart value > 100 euros
    # If cart value < 10 euro -> surcharge fee adding
    if delivery.cart_value >= 10000:
        return 0
    elif delivery.cart_value < 1000:
        delivery_fee += (1000 - delivery.cart_value) / 100

    # Distance calculations
    if(delivery.delivery_distance <= 1000):
        delivery_fee += 2
    else:
        delivery_fee += delivery.delivery_distance // 500 + min(delivery.delivery_distance % 500, 1)

    # Number of Items calculations
    if delivery.number_of_items >= 5:
        delivery_fee += (delivery.number_of_items - 4) * 0.5 + min(delivery.number_of_items//13,1) * 1.2

    # Checking for Friday Rush ( if day == Friday 15:00-19:00 )
    order_date = datetime.strptime(delivery.time, "%Y-%m-%dT%H:%M:%SZ")
    if 15 <= order_date.hour <= 17 and order_date.weekday() == 4:
        delivery_fee *= 1.2

    # Delivery fee cannot be more than 15 euro
    return min(int(delivery_fee*100), 1500)
