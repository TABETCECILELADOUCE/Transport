from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import date
app = FastAPI(title="Blog API")
#Modèle de donnée pour un article
class Article(BaseModel):
    id: Optional[int] = None
    titre: str
    contenu: str
    auteur: str
    date: date
    categorie: str
    tags: List[str]
#Base de donnée temporaire
db_article = []
# 1.Créer un article (POST)
@app.post("/api/article",status_code=201)
def create_article(article:Article):
    article.id = len(db_article) + 1
    db_article.append(article)
    return {"message": "Article créé", "id": article.id}
# 2. Lire tous les articles (GET)
@app.get("/api/article",response_model=List[Article],tags=["Articles"])
def get_articeles( categorie:Optional[str] = None):
    if categorie:
       return [a for a in db_article if a.categorie.lower() == categorie.lower()]
    return db_article
# 3. L ire un article unique par ID (GET)
@app.get("/api/articles/{article_id}")
def get_article(article_id: int):
    for a in db_article:
        if a.id == article_id:
            return 
    raise HTTPException(status_code=404,detail="Article non trouvé")
# 4. Rechercher un article(Contenu ou Titre)
@app.get("/api/articles/search",tags=["Recherche"])
def search_articles(query: str):
    results = [a for a in db_article if query.lower() in a.titre.lower() or query.lower() in a.contenu.lower()]
    return results
# 5. Modifier un article (PUT)
@app.put("/api/articles/{article_id}",tags=["Articles"])
def update_article(article_id:int, updated_article: Article):
    for i, a in enumerate(db_article):
        if a.id == article_id:
            update_article.id = article_id
            db_article[i] = update_article
            return{"message":"Article mis à jour"}
    raise HTTPException(status_code=404,detail="Article non trouvé")
# 6. Supprimer un article (DELETE)
@app.delete("/api/articles/{article_id}", tags=["Articles"])
def delete_article(article_id:int):
    for i, a in enumerate(db_article):
        if a.id == article_id:
            db_article.pop(i)
            return {"message":"L'article a été supprimé"}
    raise HTTPException(status_code=404,detail="Article non trouvé")