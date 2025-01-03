import hashlib
# print(hashlib.algorithms_available)
import json




def job6_version2(pass_user):

    caracteres_speciaux = "!@#$%^&*()-_=+[]{}|;:',.<>?/`~"
   
    if len(pass_user) < 8:
        return "mot de passe incorrect, doit contenir au moins 8 caracteres"

    if not any(caractere.isupper() for caractere in pass_user):
        return "Mot de passe incorrect : doit contenir au moins une majuscule."

    if not any(caractere.islower() for caractere in pass_user):
        return "Mot de passe incorrect : doit contenir au moins une minuscule."
    
    if not any(caractere.isdigit() for caractere in pass_user):
        return "Mot de passe incorrect : doit contenir au moins un chiffre."
    
    if not any (caractere in caracteres_speciaux for caractere in pass_user):
        return "mot de passe incorrect, doit contenir un caractere special"
    
    else:
        return "Mot de passe valide"
    
while True:
    pass_user = input("Veuillez entrer votre mot de passe:  ")
    resultat = job6_version2(pass_user)

    if resultat == "Mot de passe valide":
        print("Mot de passe valide")
        break
    else:
        print(resultat)




# Hashage
hash_data = pass_user
hashed = hashlib.sha256(hash_data.encode()).hexdigest()
print(f"CODAGE SHA-256: {hashed}")


# ecriture du mot de passe sur fichier json
def write_json():
    data = {
    "mot de passe": pass_user,
    "hash SHA 256": hashed
    }

    with open('training.json', 'r') as file:
        data = json.load(file)
    print("Contenu du fichier json",data)


    with open('training.json', 'w') as file:
        json.dump(data, file, indent=4)
        return "ecriture du mot de passe dans un fichier json"
print(write_json())


# lire le fichier json
# def read_json():
#     with open('training.json', 'r') as file:
#         data_loaded = json.load(file)
#         print("Contenu du fichier json:  ")
#         print(data_loaded)
# print(read_json())




# lire et convertir la chaine json en python
