# API de Blog -TAF 1

NOM: *TABET CECILE LADOUCE*

MATRICULE: *24G2877*

NIVEAU: L2

# Description

Ce projet est une API REST développée avec "FastAPI" permettant la gestion d'un blog.
Elle permet de créer, lire, modifier,supprimer et rechercher des articles.

# Fonctionnalités


"POST /api/article" : pour créer un nouveau article ( Renvoie le code 201).
"GET /api/article" : liste tous les articles par catégorie
"GET /api/article/search" : recherche dans les titres ou les contenus
"GET /api/article/{id}" : affiche un article spécifique 
" PUT /api/articles/{id}" : mettre à jour un article existant
" DELETE api/article/{id} : supprimer un article specifique

# INSTALLATION ET LANCEMENT



2. Activer l'environnement virtuel : " pip install fastapi uvicorn pydantic"
3. Lancer le serveur : " unicorn main:app --reload
DOCUMENTATION : une fois le serveur lancé la documentation interactive est disponible à l'adresse : http://127.0.0.1:8000/docs
