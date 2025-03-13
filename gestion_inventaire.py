list = []
e = {}
id_p = 1


def aff(list):
    if list:
        for e in list:
            print(
                f"Id :{e['id']},Nom :{e['Nom']},Quantite :{e['Quan']},Prix unitaire :{e['Prix']}DT,Status :{e['Status']}"
            )
    else:
        print("Liste Vide")
    print("\n")


def ajoutez(list, e):
    global id_p
    Nom = input("saisir Nom :")
    Quan = int(input("saisir Le Quantite :"))
    Prix = float(input("saisir Le prix Unitaire :"))
    Status = input("saisir Le Status :")

    e = {"id": id_p, "Nom": Nom, "Quan": Quan, "Prix": Prix, "Status": Status}

    list.append(e)
    id_p += 1
    print("=>Ajoutez success!\n")


def supp(list, e):
    id_n = int(input("saisir l'id du produit a supprimer :"))
    for e in list:
        if e["id"] == id_n:
            list.remove(e)
            print("=>Suppression avec success!\n")
            break
        else:
            print("=>Produit n'existe pas\n")
            break


def recherche_id(list, e):
    id_r = int(input("saisir Id du produit a rechercher :"))
    for e in list:
        if e["id"] == id_r:
            print(
                f"Nom :{e['Nom']},Quantite :{e['Quan']},Prix unitaire :{e['Prix']}DT,Status :{e['Status']}"
            )
            break
        else:
            print("ID invalide!\n")


def recherche_nom(list, e):
    nom_r = input("saisir Le Nom de Produit  a rechercher :")

    for e in list:
        if e["Nom"] == nom_r:
            print(
                f"ID :{e['id']},Quantite :{e['Quan']},Prix unitaire :{e['Prix']}DT,Status :{e['Status']}"
            )
            break
        else:
            print("Nom Invalide\n")


def enregistrer_fichier_texte(list):
    with open("/home/wassim/Desktop/wassim/Python/Inventaire.txt", "w") as f:
        for e in list:
            f.write(
                f"ID :{e['id']},Nom :{e['Nom']},Quantite :{e['Quan']},Prix unitaire :{e['Prix']}DT,Status :{e['Status']}\n"
            )
        print("=>Enregistrement avec success!\n")
        f.close()


def enregistrer_fichier_csv(list):
    with open(
        "/home/wassim/Desktop/wassim/Python/Inventaire.csv", "w", newline=""
    ) as f:
        for e in list:
            f.write(
                f"ID :{e['id']},Nom :{e['Nom']},Quantite :{e['Quan']},Prix unitaire :{e['Prix']}DT,Status :{e['Status']}\n"
            )
        print("=>Enregistrement avec success!\n")
        f.close()


def charger_fichier_csv(list):
    with open("/home/wassim/Desktop/wassim/Python//Inventaire.csv", "r") as f:
        for line in f:
            print(line)
        print("=>Chargement avec success!\n")
    f.close()


def charger_fichier_csv(list):
    with open("/home/wassim/Desktop/wassim/Python/Inventaire.csv", "r") as f:
        for line in f:
            print(line)
        print("=>Chargement avec success!\n")
    f.close()


def charger_fichier_texte(list):
    with open("/home/wassim/Desktop/wassim/Python/Inventaire.txt", "r") as f:
        for line in f:
            print(line)
        print("=>Chargement avec success!\n")
    f.close()


while True:
    print("**Bienvenue dans la gestion d'invontaire**")
    i = 1
    while i <= 10:
        print(i, "-Affichier tout les produits")
        i += 1
        print(i, "-Ajouter un nouveau Produit")
        i += 1
        print(i, "-Supprimer un produit")
        i += 1
        print(i, "-Recherche un produit par ID")
        i += 1
        print(i, "-Recherche un produit par Nom")
        i += 1
        print(i, "-Enregistrer Invontaire dans un fichier texte")
        i += 1
        print(i, "-Enregistrer Invontaire dans un fichier CSV")
        i += 1
        print(i, "-Charger Invontaires depuis un fichier text")
        i += 1
        print(i, "-charger Invontaire depuis un fichier CSV")
        i += 1
        print(i, "-Quittez")
        break

    choix = input("Saisir Votre Choix :")

    if choix == "1":
        aff(list)
    elif choix == "2":
        ajoutez(list, e)
    elif choix == "3":
        supp(list, e)
    elif choix == "4":
        recherche_id(list, e)
    elif choix == "5":
        recherche_nom(list, e)
    elif choix == "6":
        enregistrer_fichier_texte(list)
    elif choix == "7":
        enregistrer_fichier_csv(list)
    elif choix == "8":
        charger_fichier_texte(list)
    elif choix == "9":
        charger_fichier_csv(list)
    elif choix == "10":
        print("=>Programme Terminer\n")
        break
    else:
        print("Choix invalide\n")
        continue
