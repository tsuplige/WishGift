# Projet de Liste de Souhaits

Ce projet vise à créer une application de liste de souhaits qui permet aux utilisateurs de partager leurs souhaits avec leurs amis. L'objectif principal est de faciliter l'organisation des achats de cadeaux en permettant aux amis de voir ce que les autres prévoient d'acheter.

## Fonctionnalités

- **Création de Comptes Utilisateurs**: Les utilisateurs peuvent créer des comptes avec leur pseudo, adresse e-mail et mot de passe.
- **Gestion des Listes de Souhaits**: Les utilisateurs peuvent créer, modifier et supprimer leur liste de souhaits personnelle.
- **Partage des Listes de Souhaits**: Les utilisateurs peuvent partager leur liste de souhaits avec leurs amis en leur donnant accès à la visualisation.
- **Ajout d'Éléments à la Liste de Souhaits**: Les utilisateurs peuvent ajouter des éléments à leur liste de souhaits, y compris le nom de l'élément, une description, un lien vers le produit et son prix.
- **Visualisation des Listes de Souhaits des Amis**: Les utilisateurs peuvent voir les listes de souhaits de leurs amis afin de savoir quels cadeaux ils envisagent d'acheter.
- **Marquage des Éléments Comme Achetés**: Les utilisateurs peuvent marquer les éléments de leur liste de souhaits comme achetés une fois qu'ils ont été achetés, ce qui permet aux amis de voir quels éléments sont déjà pris.

## Technologies Utilisées

Ce projet est développé en utilisant les technologies suivantes :

- **Django**: Un framework web Python pour le développement rapide d'applications web.
- **HTML/CSS/JavaScript**: Pour la création de l'interface utilisateur.
- **Bootstrap**: Pour la conception et le style de l'interface utilisateur.
- **Base de Données SQLite (ou autre)**: Pour stocker les informations des utilisateurs, des listes de souhaits et des éléments.
- **Git**: Pour la gestion du code source et le contrôle de version.

## Installation

1. Cloner le dépôt GitHub sur votre machine locale.
2. Assurez-vous d'avoir Python et Django installés sur votre système.
3. Naviguez vers le répertoire du projet dans votre terminal.
4. Exécutez les commandes suivantes pour démarrer le serveur de développement :

```bash
python manage.py migrate
python manage.py runserver
```

5. Accédez à l'URL http://localhost:8000 dans votre navigateur pour accéder à l'application.

## Contributions

Les contributions à ce projet sont les bienvenues ! Si vous souhaitez contribuer, veuillez suivre ces étapes :

1. Forker le projet.
2. Créer une branche pour votre fonctionnalité (`git checkout -b fonctionnalité/nouvelle-fonctionnalité`).
3. Commiter vos modifications (`git commit -am 'Ajout d'une nouvelle fonctionnalité'`).
4. Pousser vers la branche (`git push origin fonctionnalité/nouvelle-fonctionnalité`).
5. Créer une nouvelle Pull Request.

## Auteurs

- [Thomas Supligeon](https://github.com/tsuplige) - Développeur Principal