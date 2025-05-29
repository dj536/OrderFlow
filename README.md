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


## ⚙️Installation
  ```
git clone https://github.com/votre-utilisateur/SalesTrack.git
cd SalesTrack
```
```
pip install pysqlite3
```
Vous pouvez télécharger DB Browser for SQLite ici:
```
https://sqlitebrowser.org/dl/
```


🧠Opérations sur la base de donnée
Lancez le programme
```
python3 main.py
```
Le programme:
 -Vous présente un menu qui vous donne la possibilité de:

  .faire des opérations sur la base de donnée comme des ajouts, suppressions de clients ou de produits,

  .Réaprovisionner le stock d'un produit,

  . Enregistrer une vente dont les détails seront directement stockés dans la base de donnée,

  .générer des statistiques en fonctions des données de ventes qui sont dans la base de donnée afin de faciliter la prise de décision


🧪 Exemple de Résultat après l'enregistrement d'une vente

Avant une opération d'enregistrement de vente, voila les différentes tables de la bases de donnée

![image_alt](https://github.com/dj536/SalesTrack/blob/master/images/product.png?raw=true)

![image_alt](https://github.com/dj536/SalesTrack/blob/master/images/order.png?raw=true)

![image_alt](https://github.com/dj536/SalesTrack/blob/master/images/order_detail.png?raw=true)

Avant tout achat, on remarque que dans la table product, le stock de clavier est de 23 et celui des souris sans fil Logitech est de 13.


![image_alt](https://github.com/dj536/SalesTrack/blob/master/images/new_product.png?raw=true)

![image_alt](https://github.com/dj536/SalesTrack/blob/master/images/ordersss.png?raw=true)

![image_alt](https://github.com/dj536/SalesTrack/blob/master/images/o_details.png?raw=true)


🔄 Mise à jour après enregistrement d’une vente
Avant l’enregistrement de la commande, le stock initial dans la table products était de :

Clavier : 23 unités

Souris sans fil Logitech : 13 unités

Les tables orders et order_details étaient vides car aucune vente n'avait encore été effectuée.

✅ Après l'enregistrement d'une vente (1 clavier et 1 souris sans fil Logitech) :

Les stocks ont été mis à jour automatiquement :

Clavier : passé de 23 à 22

Souris sans fil Logitech : passé de 13 à 12

Une ligne a été ajoutée dans la table orders avec :

L’ID du client

La date d’achat

Les détails de la commande ont été enregistrés dans la table order_details.


👨‍💻 Auteur

Réalisé par Justin DJIDONOU. N'hésitez pas à poser vos questions, signaler un bug ou proposer des idées.

Vos suggestions sont les bienvenues 🙂







  


