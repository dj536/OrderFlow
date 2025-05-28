# SalesTrack – Console de gestion de ventes

SalesTrack est une console de gestion qui utilise  Python et SQL pour gérér les ventes en local. Elle permet d’enregistrer automatiquement les informations liées aux produits, clients et commandes, tout en générant des statistiques pour faciliter la prise de décision.



## 📂Structure du projet
``` SalesTrack/
.
├─ my_db_create.py         # Ce fichier Python définit une classe Creadd qui a pour rôle de créer la bases de donnée.
├─ my_product_add.py       # Ce fichier permet les ajouts et suppressions de produits dans la base de données.
├─ my_client_add.py        # Ce fichier gère l'ajout et la suppression de clients dans la base de données
├─ purchase.py             # Ce fichier définit la classe Purchasing, qui permet d'enregistrer une vente (commande client) et de réapprovisionner le stock d’un produit dans la base de données.
├─ purchase_history.py     # Ce fichier définit la classe Purchase, qui permet d’afficher l’historique des commandes d’un client donné, en listant les produits achetés, leurs quantités et prix, pour chaque commande enregistrée dans la base de données.
└─ sales_report.py         # Ce fichier définit la classe Report, qui fournit des rapports analytiques sur les ventes, produits, revenus et commandes, permettant d'extraire des statistiques journalières, mensuelles ou par client à partir de la base de données.
└─ main.py                 # Ce fichier permet de tester le programme en entier.
```


## 🚀Fonctionnalités

Ajouter, supprimer des produits

Enregistrer , supprimer un client

Enregistrer une vente dans la base de données en associant un client, un ou plusieurs produits, ainsi que les quantités et le prix total.

Mettre à jour le stock de produits automatiquement

Compléter le stock de produits 

Afficher l’historique d’achat d’un client

Générer des rapports comme :
  -Nombres de commandes par jour
  -Produits les plus vendus
  -Revenu total par client
  -Nombre total de produits commandé par mois
  -Revenu total par mois
  -Top 100 des prosuits  moins populaires


## 🛠️Technologies utilisées:
  Python 3.11.9
  
  SQL
  
  sqlite3 (base de données locale)


## ⚙️ Installation
  ```
git clone https://github.com/votre-utilisateur/SalesTrack.git
cd SalesTrack
```
```
pip install pysqlite3
```


