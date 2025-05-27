from my_db_create import Creadd
import sqlite3
class Add:
    def __init__(self, db: Creadd = None):
        self.db = db 
    
    def add_customer_to_db(self):
        if not self.db.conn:
            self.db.conn = sqlite3.connect("ecom_db.db")
        if not self.db.cursor:
            self.db.cursor = self.db.conn.cursor()

        print("\n--- Ajout d’un nouveau client ---")
        name = input("name : ")
        email = input("email : ")
        phone = input("phone_number : ")
        if not phone.isdigit():
            print("Erreur : le numéro de téléphone doit contenir uniquement des chiffres.")
            return

        self.db.cursor.execute("""
            INSERT INTO customer (name, email, phone_number)
            VALUES (?, ?, ?)
        """, (name, email, phone))

        self.db.conn.commit()
        print(">> Client ajouté avec succès !")
    
    
    def del_customer_to_db(self):
        if not self.db.conn:
            self.db.conn = sqlite3.connect("ecom_db.db")
        if not self.db.cursor:
            self.db.cursor = self.db.conn.cursor()

        print("\n--- Suppression d'unclient existant---")
        id = input("id Client : ")

        self.db.cursor.execute("DELETE FROM customer WHERE id = ?", (id,))

        self.db.conn.commit()
        print(">> Client supprimé avec succès !")
"""
def main():
    
    creadd = Creadd()
    creadd.my_customer_tb_create()
    creadd.products_tb_create()
    creadd.orders_tb_create()
    creadd.orders_details_tb_create()

    add = Add(creadd)

    while True:
        print("\nBienvenue dans le système de gestion e-commerce\n")
        print("1. Ajouter un nouveau produit")
        print("2. Ajouter un nouveau client")
        print("3. Supprimer un client existant")
        print("4. Enregistrer une vente")
        print("5. Afficher l’historique d’achats d’un client")
        print("6. Rapports")
        print("7. Quitter")

        choice = input("Entrez un nombre : ")

        
        if choice == "1":
            pass
        elif choice == "2":
            add.add_customer_to_db()
        elif choice == "3":
            add.del_customer_to_db()
        
        elif choice == "6":
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Réessaie.")
    add.close_connection()


if __name__ == "__main__":
    main()
    """