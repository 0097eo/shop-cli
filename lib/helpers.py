from db.models import Customer, Shoe, Order

def exit_program():
    print("Adios!")
    exit()

def list_Customers():
    customers = Customer.get_all_customers()
    for customer in customers:
        print(customer)


def find_customer_by_name():
    name = input("Enter customer's name: ")
    customer = Customer.get_customer_by_name(name)
    print(customer) if customer else print(
        f"Customer {name} not found"
    )

def find_customer_by_id():
    customer_id = int(input("Enter customer's id: "))
    customer = Customer.get_customer_by_id(customer_id)
    print(customer) if customer else print(
        f"Customer {customer_id} not found"
    )

def create_customer():
    first_name = input("Enter customer's first name: ")
    last_name = input("Enter customer's last name: ")
    address = input("Enter customer's address: ")
    try:
        customer = Customer.create(first_name, last_name, address)
        print(f"success: {customer} created")
    except Exception as e:
        print("error creating department: ", e)

def update_customer_address():
    customer_id = input("Enter the customer's name: ")
    if customer := Customer.get_customer_by_id(customer_id):
        try:
            address = input("Enter the new address")
            customer.address = address
            customer.update_address()
            print(f"success: {customer} updated")
        except Exception as e:
            print("error updating address: ", e)
    else:
        print(f"Customer {customer_id} not found")
    

def delete_customer():
    customer_id = int(input("Enter the customer's id"))
    customer = Customer.get_customer_by_id(customer_id)
    if customer:
        customer.delete_customer()
        print(f"success: {customer} deleted")
    else:
        print(f"Customer {customer_id} not found")

def list_shoes():
    shoes = Shoe.get_all_shoes()
    for shoe in shoes:
        print(shoe)

def find_shoe_by_name():
    name = input("Enter shoe's name: ")
    shoe = Shoe.get_shoe_by_name(name)
    print(shoe) if shoe else print(
        f"Shoe {name} not found"
    )

def find_shoe_by_id():
    shoe_id = int(input("Enter shoe's id: "))
    shoe = Shoe.get_shoe_by_id(shoe_id)
    print(shoe) if shoe else print(
        f"Shoe {shoe_id} not found"
    )

def create_shoe():
    name = input("Enter shoe's name: ")
    brand = input("Enter shoe's brand: ")
    size = input("Enter shoe's size: ")
    price = input("Enter shoe's price: ")
    try:
        shoe = Shoe.create(name, brand, size, price)
        print(f"success: {shoe} created")
    except Exception as e:
        print("error creating department: ", e)

def update_shoe_price():
    shoe_id = int(input("Enter shoe's id: "))
    shoe = Shoe.get_shoe_by_id(shoe_id)
    if shoe:
        price = input("Enter shoe's new price: ")
        shoe.update_price(price)
        print(f"success: {shoe} updated")
    else:
        print(f"Shoe {shoe_id} not found")

def delete_shoe():
    shoe_id = int(input("Enter shoe's id: "))
    shoe = Shoe.get_shoe_by_id(shoe_id)
    if shoe:
        shoe.delete_shoe()
        print(f"success: {shoe} deleted")
    else:
        print(f"Shoe {shoe_id} not found")

def list_orders():
    orders = Order.get_all_orders()
    for order in orders:
        print(order)

def create_order():
    """Creates a new order for a customer and shoe."""
    customers = list_Customers() 
    customer_id = int(input("Enter customer ID from the list: "))
    customer = Customer.get_customer_by_id(customer_id)
    if not customer:
        print(f"Customer ID {customer_id} not found.")
        return

    shoes = list_shoes()
    shoe_id = int(input("Enter shoe ID from the list: "))
    shoe = Shoe.get_shoe_by_id(shoe_id)
    if not shoe:
        print(f"Shoe ID {shoe_id} not found.")
        return

    quantity = int(input("Enter order quantity: "))

    try:
        order = Order.create_order(customer, shoe, quantity)
        print(f"Success: Order {order} created.")
    except Exception as e:
        print(f"Error creating order: {e}")

def list_orders_by_customer():
    """Lists all orders for a specific customer."""
    customers = list_Customers()
    customer_id = int(input("Enter customer ID from the list: "))
    customer = Customer.get_customer_by_id(customer_id)
    if not customer:
        print(f"Customer ID {customer_id} not found.")
        return

    orders = Order.get_orders_by_customer_id(customer.customer_id)
    if not orders:
        print(f"Customer {customer} has no orders.")
    else:
        print(f"Orders for customer {customer}:")
        for order in orders:
            print(order)

def list_orders_by_shoe():
    """Lists all orders for a specific shoe."""
    shoes = list_shoes()
    shoe_id = int(input("Enter shoe ID from the list: "))
    shoe = Shoe.get_shoe_by_id(shoe_id)
    if not shoe:
        print(f"Shoe ID {shoe_id} not found.")
        return

    orders = Order.get_orders_by_shoe_id(shoe.shoe_id)
    if not orders:
        print(f"Shoe {shoe} has no orders.")
    else:
        print(f"Orders for shoe {shoe}:")
        for order in orders:
            print(order)

def update_order_quantity():
    """Updates the quantity of an existing order."""
    orders = list_orders() 
    order_id = int(input("Enter order ID from the list: "))
    order = Order.get_order_by_id(order_id)
    if not order:
        print(f"Order ID {order_id} not found.")
        return

    new_quantity = int(input("Enter new order quantity: "))

    try:
        order.quantity = new_quantity
        order.save()  
        print(f"Success: Order {order} quantity updated.")
    except Exception as e:
        print(f"Error updating order quantity: {e}")

def delete_order():
    """Deletes an existing order."""
    orders = list_orders() 
    order_id = int(input("Enter order ID from the list: "))
    order = Order.get_order_by_id(order_id)
    if not order:
        print(f"Order ID {order_id} not found.")
        return

    confirm = input(f"Are you sure you want to delete order {order}? (y/n): ")
    if confirm.lower() == "y":
        try:
            order.delete() 
            print(f"Success: Order {order} deleted.")
        except Exception as e:
            print(f"Error deleting order: {e}")