from my_db_create import Creadd
import sqlite3
class Addd:
    def __init__(self, db: Creadd = None):
        self.db = db 
    
    
    
    def add_product_to_db(self):
        if not self.db.conn:
            self.db.conn = sqlite3.connect("ecom_db.db")
        if not self.db.cursor:
            self.db.cursor = self.db.conn.cursor()

        print("\n--- Ajout d’un nouveau produit ---")
        nom = input("name : ")
        prix = input("price : ")
        stock = int (input("stock : "))

        self.db.cursor.execute("""
            INSERT INTO products (name, price, stock)
            VALUES (?, ?, ?)
        """, (nom, prix, stock))

        self.db.conn.commit()
        print(">> Produit ajouté avec succès !")

    
    def del_product_to_db(self):
        if not self.db.conn:
            self.db.conn = sqlite3.connect("ecom_db.db")
        if not self.db.cursor:
            self.db.cursor = self.db.conn.cursor()

        print("\n--- Suppression d'un produit existant---")
        id = input("id Produit : ")

        self.db.cursor.execute("DELETE FROM products WHERE product_id = ?", (id,))

        self.db.conn.commit()
        print(">> Produit supprimé avec succès !")

            
    def close_connection(self):
        if self.db.cursor:
            self.db.cursor.close()
        if self.db.conn:
            self.db.conn.close()
