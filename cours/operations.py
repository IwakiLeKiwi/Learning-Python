# coding:utf-8

"""
Opérateurs en Python : + (addition)
                       - (soustraction)
                       * (multiplication)
                       / (division)
                       % (modulo) -> reste d'une division Euclidienne

variable = variable + X
variable += X

variable = variable - X
variable -= X

variable = variable * X
variable *= X
"""

nombreA = 5  # définir des variables
nombreB = 2
resultat = nombreA / nombreB  # utiliser un opérateur
resultat = int(resultat)
reste = nombreA % nombreB  # utiliser un opérateur
reste = int(reste)

print(f"Le calcul est {nombreA} / {nombreB}")  # afficher dans la console
print("Résultat :", resultat, "Reste :", reste)

niveauPersonnage = input("Niveau de départ : ")  # lire la donnée renseignée
niveauPersonnage = int(niveauPersonnage)  # convertir la donnée en int (nombre entier)

print("Niveau personnage :", niveauPersonnage)  # afficher dans la console

print("Combat réussi, tu gagnes un niveau !")
niveauPersonnage += 1  # ajouter 1 à la donnée renseignée par l'utilisateur
# aussi possible -> niveauPersonnage = niveauPersonnage + 1

print("Niveau personnage :", niveauPersonnage)