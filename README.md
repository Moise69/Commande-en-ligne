
Projet Framework Python

1. Introduction
•	Objectif du projet :
Mon projet consiste à développer une application web de commande dans un restaurant en ligne. Les utilisateurs pourront consulter le menu, passer des commandes, et un système de gestion permettra à l'administrateur du restaurant de gérer les commandes et le menu.

2. Technologies utilisées :
	Backend : Django
	Frontend : HTML, CSS, Bootstrap, JavaScript
	Base de données : SQLite 
	Système de paiement: MVola ou Orange Money pour intégrer un paiement en ligne
3. Architecture de l'application
L'architecture de l'application sera divisée en plusieurs composants principaux :
	Frontend : La partie visible de l'application où les utilisateurs peuvent interagir.

	Backend : La partie qui gère la logique métier, les commandes, la gestion des utilisateurs, etc.


	Base de données : Où sont stockées les informations sur les utilisateurs

 Diagramme de l'architecture :

Explication
	
•	Frontend :	
Le frontend sera une interface simple pour afficher le menu, les commandes et permettre aux utilisateurs de s’inscrire, se connecter, et passer des commandes.

•	Backend :
Le backend sera construit avec Django. Django est un framework Python qui gère les bases de données via son ORM et facilite la création de vues, modèles et routes.

•	Base de données :
Les informations relatives aux utilisateurs, aux plats du menu, aux commandes et à l’historique seront stockées dans la base de données. Django utilise par défaut SQLite, mais peut aussi être configuré pour utiliser d'autres bases comme PostgreSQL ou MySQL.

4. Fonctionnalités principales de l'application :
Page d’accueil :
Affiche un menu de plats et de boissons disponibles.
Options de tri et de filtre des plats par catégorie (entrée, plat principal, dessert, etc.).
Affichage des promotions et des informations sur le restaurant.
Gestion des utilisateurs :
Système d’inscription, de connexion et de gestion de profil pour les clients.
Possibilité de réinitialiser le mot de passe.
Commande en ligne :
Les utilisateurs peuvent ajouter des plats à leur panier.
Les utilisateurs peuvent passer commande et choisir de la retirer sur place ou de se faire livrer.
Gestion des commandes :
Les commandes sont envoyées à l’administration du restaurant pour être traitées.
L’administrateur peut visualiser, modifier et marquer les commandes comme "terminées" ou "en préparation".
Paiement en ligne:
Intégration d'un système de paiement  pour le règlement des commandes en ligne.

