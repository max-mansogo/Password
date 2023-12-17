import hashlib

def vérifier_mot_de_passe(mot_de_passe):
    while True:
        if len(mot_de_passe) < 8:
            print("Le mot de passe doit contenir au moins huit caractères.")
        elif not any(c.isupper() for c in mot_de_passe):
            print("Le mot de passe doit contenir au moins une lettre majuscule.")
        elif not any(c.islower() for c in mot_de_passe):
            print("Le mot de passe doit contenir au moins une lettre minuscule.")
        elif not any(c.isdigit() for c in mot_de_passe):
            print("Le mot de passe doit contenir au moins un chiffre.")
        elif not any(c in "!@#$%^&*" for c in mot_de_passe):
            print("Le mot de passe doit contenir au moins un caractère spécial (!, @, #, $, %, ^, &, *).")
        else:
            return mot_de_passe
        mot_de_passe = input("Veuillez choisir un nouveau mot de passe : ")

def encrypter_mot_de_passe(mot_de_passe):
    objet_hash = hashlib.sha256(mot_de_passe.encode())
    mot_de_passe_encrypté = objet_hash.hexdigest()
    return mot_de_passe_encrypté

mot_de_passe = input("Veuillez choisir un mot de passe sécurisé : ")
mot_de_passe_valide = vérifier_mot_de_passe(mot_de_passe)
mot_de_passe_encrypté = encrypter_mot_de_passe(mot_de_passe_valide)

print("Mot de passe valide !")
print("Mot de passe encrypté :", mot_de_passe_encrypté)
