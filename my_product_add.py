from my_db_create import Creadd
from my_client_add import Add
import sqlite3
class Addd:
    def __init__(self, db: Creadd = None):
        self.db = db 
    
    def open_connection_if_needed(self):
        if not self.db.conn:
            self.db.conn = sqlite3.connect("ecom_db.db")
        if not self.db.cursor:
            self.db.cursor = self.db.conn.cursor()
    
    
    def print_customers(self):
        self.open_connection_if_needed()

        print("\n--- Liste des PRODUIS en base ---")
        self.db.cursor.execute("SELECT * FROM products")
        rows = self.db.cursor.fetchall()
        for row in rows:
            print(row)
    
    def add_product_to_db(self):
        if not self.db.conn:
            self.db.conn = sqlite3.connect("ecom_db.db")
        if not self.db.cursor:
            self.db.cursor = self.db.conn.cursor()

        print("\n--- Ajout d’un nouveau produit ---")
        nom = input("name : ")
        prix = input("price : ")
        stock = input("stock : ")

        self.db.cursor.execute("""
            INSERT INTO products (name, price, stock)
            VALUES (?, ?, ?)
        """, (nom, prix, stock))

        self.db.conn.commit()
        print(">> Produit ajouté avec succès !")
        self.print_customers()

    
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
        self.db.conn.close()

def main():
    
    creadd = Creadd()
    creadd.my_customer_tb_create()
    creadd.products_tb_create()
    creadd.orders_tb_create()
    creadd.orders_details_tb_create()
    add = Add(creadd)
    addd = Addd(creadd)


    while True:
        print("\nBienvenue dans le système de gestion e-commerce\n")
        print("1. Ajouter un nouveau produit")
        print("2. Supprimer un produit existant")
        print("3. Ajouter un nouveau client")
        print("4. Supprimer un client existant")
        print("5. Enregistrer une vente")
        print("6. Afficher l’historique d’achats d’un client")
        print("7. Rapports")
        print("8. Quitter")

        choice = input("Entrez un nombre : ")

        
        if choice == "1":
            addd.add_product_to_db()
        elif choice == "2":
            addd.del_product_to_db()
        elif choice == "3":
            add.add_customer_to_db()
        elif choice == "4":
            add.del_customer_to_db()
        
        elif choice == "8":
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Réessaie.")
    addd.close_connection()


if __name__ == "__main__":
    main()