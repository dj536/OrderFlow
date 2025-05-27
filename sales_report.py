from my_db_create import Creadd
import sqlite3

class Report:
    def __init__(self, db: Creadd = None):
        self.db = db

    def nombre_commandes_par_jour(self):
        date = input("entrez la date(YYY-MM-DD): ")
        if not self.db.conn:
            self.db.conn = sqlite3.connect("ecom_db.db")
        if not self.db.cursor:
            self.db.cursor = self.db.conn.cursor()
        print("\nNombre de commandes par jour :")
        self.db.cursor.execute("""
            SELECT SUBSTR(order_date, 1, 10), COUNT(*) AS nb_commandes
            FROM orders
            where SUBSTR(order_date, 1, 10) = ?
            GROUP BY order_date
        """, (date,),)
        for row in self.db.cursor.fetchall():
            print(f"{row[0]} : {row[1]} commandes")

    def produits_les_plus_vendus(self):
        if not self.db.conn:
            self.db.conn = sqlite3.connect("ecom_db.db")
        if not self.db.cursor:
            self.db.cursor = self.db.conn.cursor()
        limit=100
        print(f"\n Top {limit} produits les plus vendus :")
        self.db.cursor.execute("""
            SELECT p.name, SUM(od.quantity) AS total_vendu
            FROM order_details od
            JOIN products p ON od.id_product = p.product_id
            GROUP BY p.product_id
            ORDER BY total_vendu DESC
            LIMIT ?;
        """, (limit,))
        for row in self.db.cursor.fetchall():
            print(f"{row[0]} : {row[1]} unités vendues")

    def revenu_total_par_client(self):
        if not self.db.conn:
            self.db.conn = sqlite3.connect("ecom_db.db")
        if not self.db.cursor:
            self.db.cursor = self.db.conn.cursor()
        id_client = input("Entrez votre ID client : ")
        print("\n Revenu total par client :")
        self.db.cursor.execute("""
            SELECT c.name, SUM(od.quantity * od.price) AS revenu
            FROM orders o
            JOIN order_details od ON o.order_id = od.id_order
            JOIN customer c ON o.customer_id = c.id
            where c.id = ?
            GROUP BY c.id
        """, (id_client,))
        if not id_client:
            print("Client non trouvé. Veuillez vous enregistrer avant de passer une commande.")
            return
        for row in self.db.cursor.fetchall():
            print(f"{row[0]} : {row[1]} €")

    def produits_par_mois(self):
        mois = input("entrez le mois(YYYY-MM): ")
        if not self.db.conn:
            self.db.conn = sqlite3.connect("ecom_db.db")
        if not self.db.cursor:
            self.db.cursor = self.db.conn.cursor()
        print("\n Nombre de produits commandés par mois :")
        self.db.cursor.execute("""
            SELECT SUBSTR(order_date, 1, 7) AS mois, SUM(od.quantity)
            FROM orders o
            JOIN order_details as od ON o.order_id = od.id_order
            where o.order_date LIKE ?
            GROUP BY mois
            """, (mois + '%',))
        for row in self.db.cursor.fetchall():
            print(f"{row[0]} : {row[1]} produits")


    def revenu_par_mois(self):
        mois = input("entrez le mois(YYYY-MM): ")
        self.db.cursor.execute("""
            SELECT SUBSTR(order_date, 1, 7) AS mois, SUM(od.quantity * od.price) AS revenu
            FROM orders as  o
            JOIN order_details od ON o.order_id = od.id_order
            WHERE o.order_date LIKE ?
            GROUP BY mois
        """, (mois + '%',))
        result = self.db.cursor.fetchone()
        if result:
            print(f"Revenu pour {result[0]} : {result[1]:.2f} €")
        else:
            print("Aucune commande pour ce mois.")


    def produits_moins_populaires(self):
        if not self.db.conn:
            self.db.conn = sqlite3.connect("ecom_db.db")
        if not self.db.cursor:
            self.db.cursor = self.db.conn.cursor()
        limit=100
        print(f"\n Produits les moins populaires (top {limit}) :")
        self.db.cursor.execute("""
            SELECT p.name, IFNULL(SUM(od.quantity), 0) AS total_vendu
            FROM products p
            LEFT JOIN order_details od ON p.product_id = od.id_product
            GROUP BY p.product_id
            ORDER BY total_vendu ASC
            LIMIT ?;
        """, (limit,))
        for row in self.db.cursor.fetchall():
            print(f"{row[0]} : {row[1]} ventes")
