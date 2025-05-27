from my_db_create import Creadd

import datetime
import sqlite3


class Purchasing:
    def __init__(self, db: Creadd):
        self.db = db

    def sell_register(self):
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
        if client:
            nb_articles_str = (input("Combien d'articles voulez-vous commander ? "))    
            if not nb_articles_str.isdigit():
                print("Erreur : Invalide.")
                return
            nb_articles = int(nb_articles_str)

        total_commande = 0.0
        articles_commandes = []

        for i in range(nb_articles):
            print(f"\nArticle {i+1}:")
            product_id = input("Entrez l'ID du produit : ")
            if not product_id.isdigit():
                print("Erreur : l'ID du produit doit être un nombre entier.")
                return
            product_id = int(product_id)
            self.db.cursor.execute("SELECT stock, price, name FROM products WHERE product_id = ?", (product_id,))
            produit = self.db.cursor.fetchone()
            if not produit:
                print("Produit non trouvé.")
                return
        
            stock_dispo, prix_unitaire, nom_produit = produit
            print(f"Produit '{nom_produit}' en stock : {stock_dispo}")

            quantite_commande = input("Quantité commandée : ")
            if not quantite_commande.isdigit():
                print("Erreur :Entrez un nombre entier.")
                return
            quantite_commande = int(quantite_commande)

            if quantite_commande > stock_dispo:
                print(f"Quantité insuffisante en stock. Disponible : {stock_dispo}")
                continue
        
            total_article = quantite_commande * prix_unitaire
            total_commande += float(total_article)
        
            articles_commandes.append((product_id, quantite_commande, prix_unitaire))

        if not articles_commandes:
            print("Aucun article valide commandé, annulation de la commande.")

        
        date_commande = datetime.datetime.now().strftime("%Y-%m-%d")
        self.db.cursor.execute("INSERT INTO orders (customer_id, order_date) VALUES (?, ?)", (client_id, date_commande))
        self.db.conn.commit()

        order_id = self.db.cursor.lastrowid

        for product_id, quantite, prix_unitaire in articles_commandes:
            self.db.cursor.execute("""
                INSERT INTO order_details (id_order, id_product, quantity, price)
                VALUES (?, ?, ?, ?)
                """, (order_id, product_id, quantite, prix_unitaire))

            self.db.cursor.execute("""
                UPDATE products SET stock = stock - ? WHERE product_id = ?
                """, (quantite, product_id))
    
        self.db.conn.commit()

        print(f"Commande enregistrée avec succès ! Total à payer : {total_commande:.2f} €")



    def add_product_stock(self):
        if not self.db.conn:
            self.db.conn = sqlite3.connect("ecom_db.db")
        if not self.db.cursor:
            self.db.cursor = self.db.conn.cursor()

        product_id = input("Entrez l'ID du produit à réapprovisionner : ")
        self.db.cursor.execute("SELECT name, stock FROM products WHERE product_id = ?", (product_id,))
        produit = self.db.cursor.fetchone()

        if not produit:
            print("Produit non trouvé.")
            return

        nom, stock_actuel = produit
        print(f"Produit : {nom} | Stock actuel : {stock_actuel}")

        
        quantite_ajoutee = int(input("Quantité à ajouter au stock : "))
        if quantite_ajoutee <= 0:
            print("La quantité doit être positive.")
            return
   
        self.db.cursor.execute("""
            UPDATE products SET stock = stock + ? WHERE product_id = ?
            """, (quantite_ajoutee, product_id))

        self.db.conn.commit()
        print(f"Stock mis à jour. Nouveau stock : {stock_actuel + quantite_ajoutee}")
