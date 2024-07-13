def rechercherproduit_par_nom():
    with open('articles.json', 'r') as fichier:
        articles = json.load(fichier)
    recherche_art = input("Saisissez le nom de l'article à rechercher :")
    i = 0
    while(i <= len(articles)-1):
        if recherche_art == articles[i] ['nom']:
            print("Le nom de l'article :", articles[i]['nom'],"Le prix de l'article :", articles[i]['prix'])
            return i -1
        elif (i != len(articles)-1):
            i += 1
        else:
            print("Le nom de l'article n'est pas trouvé")
            break