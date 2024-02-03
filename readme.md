# Gestion de Stock

Cette application de gestion de stock est développée en utilisant le langage de programmation Python et la bibliothèque Qt (PySide6) pour l'interface utilisateur. Elle permet aux utilisateurs de suivre les produits, les catégories, d'ajouter, de modifier, de supprimer des produits, et d'exporter les données au format CSV.

## Configuration requise

- Python 3.x
- Bibliothèque PySide6
- Serveur MySQL (ou un autre système de gestion de base de données pris en charge)

## Installation

1. Clonez le dépôt :
    ```bash
    git clone https://github.com/votre_utilisateur/gestion-de-stock.git
    cd gestion-de-stock
    ```

2. Installez les dépendances :
    ```bash
    pip install -r requirements.txt
    ```

## Utilisation

1. Assurez-vous que votre serveur MySQL est en cours d'exécution.

2. Exécutez l'application :
    ```bash
    python run.py
    ```

3. L'interface de l'application s'ouvrira, vous permettant de gérer votre stock.

## Fonctionnalités

- **Ajouter/Modifier/Supprimer un produit :** Remplissez les détails dans le formulaire à droite et cliquez sur le bouton "Ajouter" ou "Modifier". Pour supprimer un produit, sélectionnez-le dans la liste et cliquez sur "Supprimer".

- **Nouvelle Catégorie :** Cliquez sur le bouton "Nouvelle Catégorie" pour créer une nouvelle catégorie.

- **Exporter en CSV :** Exportez les données actuelles vers un fichier CSV en cliquant sur le bouton correspondant.

- **Filtrer par catégorie :** Utilisez le menu déroulant pour filtrer les produits par catégorie.

- **Supprimer :** Le bouton "Supprimer" permet de supprimer le produit sélectionné.
