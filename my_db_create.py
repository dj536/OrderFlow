import sqlite3

class Creadd:
    def __init__(self, conn: sqlite3.Connection = None, cursor: sqlite3.Cursor = None ):
        self.conn = conn
        self.cursor = cursor

    def my_customer_tb_create(self):
        if not self.conn:
            self.conn = sqlite3.connect("ecom_db.db")
        if not self.cursor:
            self.cursor = self.conn.cursor()
        self.cursor.execute("""create table if not exists customer(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name varchar(255),
                       email varchar(255),
                       phone_number varchar(255)
                       )""")
        self.conn.commit()

    def products_tb_create(self):
        if not self.conn:
            self.conn = sqlite3.connect("ecom_db.db")
        if not self.cursor:
            self.cursor = self.conn.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS products(
                       product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name VARCHAR(255),
                       price float,
                       stock INT
                       )""")
        self.conn.commit()

    def orders_tb_create(self):
        if not self.conn:
            self.conn = sqlite3.connect("ecom_db.db")
        if not self.cursor:
            self.cursor = self.conn.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS orders(
                       order_id INTEGER PRIMARY KEY AUTOINCREMENT,
                       customer_id int,
                       order_date DATE,
                       FOREIGN KEY(customer_id) REFERENCES customer(id)
                       )""")
        self.conn.commit()
    
    def orders_details_tb_create(self):
        if not self.conn:
            self.conn = sqlite3.connect("ecom_db.db")
        if not self.cursor:
            self.cursor = self.conn.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS order_details(
                       id_details INTEGER PRIMARY KEY AUTOINCREMENT,
                       id_order INTEGER,
                       id_product INTEGER,
                       quantity INT,
                       price float,
                       FOREIGN KEY(id_order) REFERENCES orders(order_id),
                       FOREIGN KEY(id_product) REFERENCES products(product_id)

                       )""")
        self.conn.commit()

    def close_connection(self):
        self.conn.close()

#creadd = Creadd()
#creadd.my_customer_tb_create()
#creadd.products_tb_create()
#creadd.orders_tb_create()
#creadd.orders_details_tb_create()
#creadd.close_connection()
