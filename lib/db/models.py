from connection import CONN, CURSOR

class Shoe:
    all = []
    def __init__(self, shoe_id, name, brand, size, price):
        self.shoe_id = shoe_id
        self.name = name
        self.brand = brand
        self.size = size
        self.price = price

    def __repr__(self):
        return f"<Shoe: {self.shoe_id}, {self.name}, {self.brand}, {self.size}, {self.price}>"

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if hasattr(self, '_name'):
            raise AttributeError("Name cannot be changed once instantiated")
        else:
            if isinstance(new_name, str):
                self._name = new_name
            else:
                raise TypeError("Name must be a string")
            
    @property
    def brand(self):
        return self._brand
    
    @brand.setter
    def brand(self, new_brand):
        if hasattr(self, '_brand'):
            raise AttributeError("Brand cannot be changed once instantiated")
        else:
            if isinstance(new_brand, str):
                self._brand = new_brand
            else:
                raise TypeError("Brand must be a string")
            
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, new_size):
        if hasattr(self, '_size'):
            raise AttributeError("Size cannot be changed once instantiated")
        else:
            if isinstance(new_size, int):
                self._size = new_size
            else:
                raise TypeError("Size must be an integer")
            
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price):
        if isinstance(new_price, int):
            self._price = new_price
        else:
            raise TypeError("Price must be a integer")
        
    @classmethod
    def create_shoe_table(cls, name, brand, size, price):
        sql = """
            CREATE TABLE IF NOT EXISTS shoes (
            shoe_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            brand TEXT,
            size INTEGER,
            price INTEGER
            )
        """
        CURSOR.execute(sql)
        CONN.commit()
        return cls(CURSOR.lastrowid, name, brand, size, price)
    
    def save_shoe(self):
        sql = """
            INSERT INTO shoes (name, brand, size, price)
            VALUES (?,?,?,?)
        """
        CURSOR.execute(sql, (self.name, self.brand, self.size, self.price))
        CONN.commit()

        type(self).all[CURSOR.lastrowid] = self

    def update_price(self):
        sql = """
            UPDATE shoes
            SET price = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.price,))
        CONN.commit()

    def delete_shoe(self):
        sql = """
            DELETE FROM shoes
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.shoe_id))
        CONN.commit()
        del type(self).all[self.shoe_id]
        self.shoe_id = None

    @classmethod
    def create(cls, name, brand, size, price):
        shoe = cls(name, brand, size, price)
        shoe.save_shoe()
        return shoe
    
    @classmethod
    def instance_of_shoe(cls, row):
        shoe = cls.all.get(row[0])
        if shoe:
            shoe.name = row[1]
            shoe.brand = row[2]
            shoe.size = row[3]
            shoe.price = row[4]
        else:
            shoe = cls (row[1], row[2], row[3], row[4])
            shoe_id = row[0]
            cls.all[shoe_id] = shoe
        return shoe
    
    @classmethod
    def get_all_shoes(cls):
        sql = """
            SELECT * FROM shoes
        """
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()
        return [cls.instance_of_shoe(row) for row in rows]
    
    @classmethod
    def get_shoe_by_id(cls, shoe_id):
        sql = """
            SELECT * FROM shoes
            WHERE id = ?
        """
        CURSOR.execute(sql, (shoe_id,))
        row = CURSOR.fetchone()
        return cls.instance_of_shoe(row) if row else None
    
    @classmethod
    def get_shoe_by_name(cls, name):
        sql = """
            SELECT * FROM shoes
            WHERE name =?
        """
        CURSOR.execute(sql, (name,))
        row = CURSOR.fetchone()
        return cls.instance_of_shoe(row) if row else None
    

class Customer:
    all = []
    def __init__(self, customer_id, first_name, last_name, address):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

    def __repr__(self):
        return f"<Customer: {self.customer_id}, {self.first_name}, {self.last_name}, {self.address}>"
    

    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, new_first_name):
        if hasattr(self, '_first_name'):
            raise AttributeError("First name cannot be changed once instantiated")
        else:
            if isinstance(new_first_name, str):
                self._first_name = new_first_name
            else:
                raise TypeError("First name must be a string")
            
    
    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, new_last_name):
        if hasattr(self, '_last_name'):
            raise AttributeError("Last name cannot be changed once instantiated")
        else:
            if isinstance(new_last_name, str):
                self._last_name = new_last_name
            else:
                raise TypeError("Last name must be a string")
            
    @property
    def address(self):
        return self._address
    
    @address.setter
    def address(self, new_address):
        if isinstance(new_address, str):
            self._address = new_address
        else:
            raise TypeError("Adress must be a string")
        
    @classmethod
    def create_customer_table(cls, first_name, last_name, address):
        sql = """
            CREATE TABLE IF NOT EXISTS customers (
            customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            address TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()
        return cls(CURSOR.lastrowid, first_name, last_name, address)
    

    def save_customer(self):
        sql = """
            INSERT INTO customers (first_name, last_name, address)
            VALUES (?,?,?)
        """
        CURSOR.execute(sql, (self.first_name, self.last_name, self.address))
        CONN.commit()

        type(self).all[CURSOR.lastrowid] = self

    def update_address(self):
        sql = """
            UPDATE customers
            SET address = ?
            WHERE id =?
        """
        CURSOR.execute(sql, (self.address,))
        CONN.commit()

    def delete_customer(self):
        sql = """
            DELETE FROM customers
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.customer_id))
        CONN.commit()
        del type(self).all[self.customer_id]
        self.customer_id = None


    @classmethod
    def create(cls, first_name, last_name, address):
        shoe = cls(first_name, last_name, address)
        shoe.save_customer()
        return shoe


    def instance_of_customer(cls, row):
        customer = cls.all.get(row[0])
        if customer:
            customer.first_name = row[1]
            customer.last_name = row[2]
            customer.address = row[3]
        else:
            customer = cls (row[1], row[2], row[3])
            customer_id = row[0]
            cls.all[customer_id] = customer
        return customer

    @classmethod
    def get_all_customers(cls):
        sql = """
            SELECT * FROM customers
        """
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()
        return [cls.instance_of_customer(row) for row in rows]  # unpacking row using *

    @classmethod
    def get_customer_by_id(cls, customer_id):
        sql = """
            SELECT * FROM customers
            WHERE id =?
        """
        CURSOR.execute(sql, (customer_id,))
        row = CURSOR.fetchone()
        return cls.instance_of_customer(row)
    
    @classmethod
    def get_customer_by_name(cls, name):
        sql = """
            SELECT * FROM customers
            WHERE first_name =?
        """
        CURSOR.execute(sql, (name,))
        row = CURSOR.fetchone()
        return cls.instance_of_customer(row) if row else None
    

class Order:
    def __init__(self, order_id, customer, shoe, quantity):
        self.order_id = order_id
        self.customer = customer
        self.shoe = shoe
        self.quantity = quantity

    def __repr__(self):
        return f"<Order: {self.order_id}, Customer: {self.customer}, Shoe: {self.shoe}, Quantity: {self.quantity}>"

    @classmethod
    def create_order_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS orders (
            order_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER FOREIGN KEY REFERENCES customers(customer_id),
            shoe_id INTEGER FOREIGN KEY REFERENCES shoes(shoe_id),
            quantity INTEGER
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create_order(cls, customer, shoe, quantity):
        sql = """
            INSERT INTO orders (customer_id, shoe_id, quantity)
            VALUES (?,?,?)
        """
        CURSOR.execute(sql, (customer.customer_id, shoe.shoe_id, quantity))
        CONN.commit()
        return cls(CURSOR.lastrowid, customer, shoe, quantity)

    @classmethod
    def get_all_orders(cls):
        sql = """
            SELECT * FROM orders
        """
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()
        return [cls(*row) for row in rows]  # unpacking row using *

    @classmethod
    def get_order_by_id(cls, order_id):
        sql = """
            SELECT * FROM orders
            WHERE order_id = ?
        """
        CURSOR.execute(sql, (order_id,))
        row = CURSOR.fetchone()
        if row:
            return cls(*row)  # unpacking row using *
        else:
            return None

    @classmethod
    def get_orders_by_customer_id(cls, customer_id):
        sql = """
            SELECT * FROM orders
            WHERE customer_id = ?
        """
        CURSOR.execute(sql, (customer_id,))
        rows = CURSOR.fetchall()
        return [cls(*row) for row in rows]  # unpacking row using *

    @classmethod
    def get_orders_by_shoe_id(cls, shoe_id):
        sql = """
            SELECT * FROM orders
            WHERE shoe_id = ?
        """
        CURSOR.execute(sql, (shoe_id,))
        rows = CURSOR.fetchall()
        return [cls(*row) for row in rows]
