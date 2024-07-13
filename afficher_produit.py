def afficherProduit():
    with open('articles.json','r') as fichier:
        articles = json.load(fichier)
   
    for article in articles:
        id_article = article.get('id article', 'N/A')
        nomArt = article.get('nom', 'N/A')
        prixArt = article.get('prix', 'N/A')
        qteArt = article.get('quantité', 'N/A')
        print(f"ID {id_article} - Nom de l'article: {nomArt}, Prix: {prixArt}, Quantité: {qteArt}")
    print("\n",len(articles))
