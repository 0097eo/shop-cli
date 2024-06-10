class Shoe:
    def __init__(self, shoe_id, name, brand, size, price):
        self.shoe_id = shoe_id
        self.name = name
        self.brand = brand
        self.size = size
        self.price = price
    

class Customer:
    def __init__(self, customer_id, first_name, last_name):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name


class Orders:
    def __init__(self, order_id, customer_id, shoe_id, quantity):
        self.order_id = order_id
        self.customer_id = customer_id
        self.shoe_id = shoe_id
        self.quantity = quantity
