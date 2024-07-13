import json
articles = []
id_article = 1

def validationNomArticle(nomArt):
    test = nomArt.isnumeric()
    while test == True:
        prixArt = input("Erreur veuillez entrez un nom valide valide :")
        test = prixArt.isnumeric()
        if test == False:
            break

def validationPrixArticle(prixArt):
    test = prixArt.isdecimal()
    while test == False:
        prixArt = input("Erreur veuillez entrez un prix valide :")
        test = prixArt.isdecimal()
        if test == True:
            break
def validationQteArticle(qteArt):
    test = qteArt.isnumeric()
    while test == False:
        prixArt = input("Erreur veuillez entrez une quantité valide :")
        test = prixArt.isnumeric()
        if test == True:
            break

def ajoutArticle():
    global articles
    global nomArt    
    global prixArt
    global qteArt
    global id_article
    #numArt = input("Saisir le numero de l'article :")
    nomArt = input("Saisir le nom de l'article :")
    validationNomArticle(nomArt)
    prixArt = input("Saisir le prix de l'article :")
    validationPrixArticle(prixArt)
    qteArt = input("Saisir la quantité de l'article :")
    validationQteArticle(qteArt)
    id_article += 1
    article = {"id article": id_article , "nom": nomArt,"prix": prixArt,"quantité": qteArt}
    
    try:
        with open("articles.json", "r") as fichier:
            articles = json.load(fichier)
    except FileNotFoundError:
        articles = []
    articles.append(article)
    id_article = len(articles) + 1
    
    
    with open("articles.json","w") as fichier:
        json.dump(articles, fichier,indent=1)