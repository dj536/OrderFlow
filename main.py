from my_db_create import Creadd
from my_client_add import Add
from purchase import Purchasing
from purchase_history import Purchase
from sales_report import Report
from my_product_add import Addd
def main():
    
    creadd = Creadd()
    creadd.my_customer_tb_create()
    creadd.products_tb_create()
    creadd.orders_tb_create()
    creadd.orders_details_tb_create()
    add = Add(creadd)
    addd = Addd(creadd)
    adddd = Purchasing(creadd)
    hst_pchs = Purchase(creadd)
    rprt = Report(creadd)

    while True:
        print("\nBienvenue dans le système de gestion e-commerce\n")
        print("1. Ajouter un nouveau produit")
        print("2. Supprimer un produit existant")
        print("3. Ajouter un nouveau client")
        print("4. Supprimer un client existant")
        print("5. Enregistrer une vente")
        print("6. Completer le stock d'un produit")
        print("7. Afficher l’historique d’achats d’un client")
        print("8. Rapports")
        print("9. Quitter")

        choice = input("Entrez un nombre : ")

        
        if choice == "1":
            addd.add_product_to_db()
        elif choice == "2":
            addd.del_product_to_db()
        elif choice == "3":
            add.add_customer_to_db()
        elif choice == "4":
            add.del_customer_to_db()
        elif choice == "5":
            adddd.sell_register()
        elif choice == "6":
            adddd.add_product_stock()
        elif choice == "7":
            hst_pchs.history()
        elif choice == "8":
            while True:
                print("\nRapports\n")
                print("1. Nombres de commandes par jour")
                print("2. Produits les plus vendus")
                print("3. Revenu total par client")
                print("4. Nombre total de produits commandé par mois")
                print("5. Revenu total par mois")
                print("6. Top 100 des prosuits  moins populaires")
                print("7. Quitter")
                my_choice = input("Entrez un nombre : ")
                if my_choice == "1":
                    rprt.nombre_commandes_par_jour()
                elif my_choice == "2":
                    rprt.produits_les_plus_vendus()
                elif my_choice == "3":
                    rprt.revenu_total_par_client()
                elif my_choice == "4":
                    rprt.produits_par_mois()
                elif my_choice == "5":
                    rprt.revenu_par_mois()
                elif my_choice == "6":
                    rprt.produits_moins_populaires()
                elif my_choice == "7":
                    print("bye")
                    break
        elif choice == "9":
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Réessaie.")
    addd.close_connection()


if __name__ == "__main__":
    main()