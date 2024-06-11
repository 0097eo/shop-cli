from db.models import Shoe, Customer, Order

def seed():
    Shoe.create_shoe_table()
    Customer.create_customer_table()
    Order.create_order_table()

    # Create shoe seed data
    shoe1 = Shoe.create("Running Shoe", "Adidas", 8, 120)
    shoe2 = Shoe.create("Basketball Shoe", "Nike", 10, 150)
    shoe3 = Shoe.create("Walking Shoe", "New Balance", 7, 80)

    # Create customer seed data
    customer1 = Customer.create("John", "Doe", "123 Main St")
    customer2 = Customer.create("Jane", "Smith", "456 Elm St")

    # Create order seed data (assuming customers and shoes already exist)
    Order.create_order(customer1, shoe1, 2)  # John Doe buys 2 running shoes
    Order.create_order(customer2, shoe2, 1)  # Jane Smith buys 1 basketball shoe

    print("Database seeded successfully!")

if __name__ == "__main__":
    seed()
