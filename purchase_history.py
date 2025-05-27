from my_db_create import Creadd

import datetime
import sqlite3


class Purchase:
    def __init__(self, db: Creadd):
        self.db = db

    def history(self):
        if not self.db.conn:
            self.db.conn = sqlite3.connect("ecom_db.db")
        if not self.db.cursor:
            self.db.cursor = self.db.conn.cursor()

        client_id = input("Entrez votre ID client : ")
        self.db.cursor.execute("SELECT * FROM customer WHERE id = ?", (client_id,))
        client = self.db.cursor.fetchone()
        if not client:
            print("Client non trouvé. Veuillez vous enregistrer avant de passer une commande.")
            return
        print(f"\nHistorique des achats pour le client : {client[0]}\n")

        self.db.cursor.execute("""
            SELECT o.order_id, o.order_date, p.name, od.quantity, od.price
            FROM orders as o
            JOIN order_details od ON o.order_id = od.id_order
            JOIN products p ON od.id_product = p.product_id
            WHERE o.customer_id = ?
            """, (client_id,))
        result = self.db.cursor.fetchall()

        if not result:
            print("Aucune commande trouvée.")
            return

        last_id = None
        for id_order, date, nom, quantite, prix in result:
            if id_order != last_id:
                print(f"\nCommande {id_order} - Date : {date}")
                last_id = id_order
            print(f" - {nom} | Qté : {quantite} | Prix unitaire : {prix} €")

