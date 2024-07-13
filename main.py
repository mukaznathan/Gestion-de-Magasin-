from articles import *

def supprimer_doublons(tab):
    tab1 = []
    for i in tab1:
        if i not in tab1:
            tab1.append(i)
    print(tab1)
def menu_principal():
    print("1. Ajouter produit")
    print("2. Afficher produits")
    print("3. Rechercher produit")
    print("4. Enregistrer vente")
    print("5. Afficher ventes")
    print("6. Ventes par client")
    print("7. Générer rapport de ventes")
    print("8. Charger données")
    print("9. Quitter")
    return input("Choisissez une option: ")



def main():
    #charger_donnees()
    while True:
        choix = menu_principal()
        if choix == '1':
            #interface_ajout_produit()
            ajoutArticle()
            
        elif choix == '2':
            #interface_affichage_produits()
            print("interface_affichage_produits")
            afficherProduit()
        elif choix == '3':
            #interface_recherche_produit()
            print("interface_affichage_produits")
            
            rechercherproduit_par_nom()
        elif choix == '4':
            #interface_enregistrement_vente()
            print("interface_affichage_produits")
            enregistrer_vente()
        elif choix == '5':
            #interface_affichage_ventes()
            print("interface_affichage_produits")
            afficher_ventes()
        elif choix == '6':
            #interface_ventes_par_client()
            print("interface_affichage_produits")
        elif choix == '7':
            #generer_rapport_ventes()
            print("interface_affichage_produits")
        elif choix == '8':
            #charger_donnees()
            print("interface_affichage_produits")
        elif choix == '9':
            break
        else:
            print("Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()