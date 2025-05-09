# LITRevu - Application Django

Projet réalisé dans le cadre du parcours Développeur d’application Python (OpenClassrooms).

## Objectif

Créer une application web permettant aux utilisateurs de :
- Publier des demandes de critique de livres ou d'articles (tickets)
- Répondre à ces demandes via des critiques (reviews)
- Suivre d’autres utilisateurs pour voir leurs publications dans un fil d’actualité personnalisé

---

## Installation et configuration

### 1. Cloner le projet

```bash
git clone https://github.com/niss-tech/project_9_opc.git
cd project_9_opc
```

### 2. Créer un environnement virtuel

```bash
python -m venv env
source env/bin/activate  # Sur Windows : env\Scripts\activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Lancer le serveur

```bash
python manage.py migrate
python manage.py runserver
```

---

## Structure du projet

- `authentication` : gestion des utilisateurs (inscription, connexion, accueil)
- `tickets` : publication et gestion des billets
- `review` : création, modification, suppression de critiques
- `follows` : suivre ou ne plus suivre d’autres utilisateurs
- `litreview` : configuration principale du projet Django

---

## Fonctionnalités

- Inscription / Connexion / Déconnexion
- Créer un ticket (demande de critique)
- Répondre à un ticket (review liée)
- Noter avec un système d’étoiles
- Voir les publications dans un flux personnalisé (fil d’actualité)
- Voir ses propres publications
- Suivre et ne plus suivre d’utilisateurs
- Interface responsive et design inspiré de wireframes

---

## Accessibilité

Le site respecte les bonnes pratiques d’accessibilité WCAG :
- Labels associés aux champs de formulaire
- Contraste suffisant
- Navigation claire avec tabulation

---

## Tests et qualité du code

- Vérification PEP8 avec Flake8 (`flake8 .`)
- Nettoyage des lignes trop longues (> 79 caractères)
- Nettoyage des imports inutiles
- Fichiers CSS bien séparés

---


**Nisrine Adamo**