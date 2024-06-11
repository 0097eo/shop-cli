from helpers import (
    exit_program,
    list_Customers,
    find_customer_by_name,
    find_customer_by_id,
    create_customer,
    update_customer_address,
    delete_customer,
    list_shoes,
    find_shoe_by_name,
    find_shoe_by_id,
    create_shoe,
    update_shoe_price,
    delete_shoe,
    list_orders,
    create_order,
    list_orders_by_customer,
    update_order_quantity,
    delete_order
)

def main():
    while True:
        menu()
        choice = input(">")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_Customers()
        elif choice == "2":
            find_customer_by_name()
        elif choice == "3":
            find_customer_by_id()
        elif choice == "4":
            create_customer()
        elif choice == "5":
            update_customer_address()
        elif choice == "6":
            delete_customer()
        elif choice == "7":
            list_shoes()
        elif choice == "8":
            find_shoe_by_id()
        elif choice == "9":
            find_shoe_by_name()
        elif choice == "10":
            create_shoe()
        elif choice == "11":
            delete_shoe()
        elif choice == "12":
            update_shoe_price()
        elif choice == "13":
            list_orders()
        elif choice == "14":
            list_orders_by_customer()
        elif choice == "15":
            create_order()
        elif choice == "16":
            update_order_quantity()
        elif choice == "17":
            delete_order()
        


def menu():
    print("What do you want to do?: ")
    print("0. Quit")
    print("1. List all Customers")
    print("2. Find Customer by Name")
    print("3. Find Customer by ID")
    print("4. Create Customer")
    print("5. Update Customer Address")
    print("6. Delete Customer")
    print("7. List all Shoes")
    print("8. Find Shoe by ID")
    print("9. Find Shoe by Name")
    print("10. Add a new Shoe")
    print("11. Delete Shoe")
    print("12. Update Shoe Price")
    print("13. List all Orders")
    print("14. Find Order by a Customer ID")
    print("15. Create Order")
    print("16. Update Order Quantity")
    print("17. Delete Order")

if __name__ == "__main__":
    main()

