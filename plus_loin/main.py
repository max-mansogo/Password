import json

def ajouter_mot_de_passe():
    site = input("Entrez le nom du site web : ")
    utilisateur = input("Entrez votre nom d'utilisateur : ")
    mot_de_passe = input("Entrez votre mot de passe : ")
    
    with open("mots_de_passe.json", "r") as fichier:
        mots_de_passe = json.load(fichier)
        
    mots_de_passe[site] = {"utilisateur": utilisateur, "mot_de_passe": mot_de_passe}
    
    with open("mots_de_passe.json", "w") as fichier:
        json.dump(mots_de_passe, fichier)
        
    print("Mot de passe ajouté avec succès.")

def afficher_mots_de_passe():
    with open("mots_de_passe.json", "r") as fichier:
        mots_de_passe = json.load(fichier)
        
    for site, donnees in mots_de_passe.items():
        print(f"Site : {site}")
        print(f"Utilisateur : {donnees['utilisateur']}")
        print(f"Mot de passe : {donnees['mot_de_passe']}")
        print()

ajouter_mot_de_passe()
afficher_mots_de_passe()
