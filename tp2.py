# Amelia Wilson 401
# tp2

# Amelia Wilson 401
# tp2

#exercice a
x = input('entrez votre nom: ')
print('hello, ' + x)

#exercice c
nombre = int(input('combiende rangées voulez vous: '))
for i in range(nombre + 1, 0,-1):
    print('*'*i)

#jeu de devinette

import random

def jeu_devinette():
    nombre_random = random.randint(0, 1000)#l'ordinateur choisit un nombre entre 0 et 1000
    print('jai choisit un nombre entre 0 et 1000.')
    essai = int(input('nombre: '))
    nb_essai = 0

    while essai != nombre_random:
        nb_essai += 1 #le nombre d'essais augmente de 1 chaque fois que le nombre n'est pas deviné

        if essai < nombre_random:
            essai = int(input("le nombre est plus grand: "))

        if essai > nombre_random:
            essai = int(input("le nombre est plus petit: "))

        if essai == nombre_random:
            print("bravo! vous avez devinez le bon nombre en " + str(nb_essai) + " essais.")
            rejouer = str(input("voulez-vous rejouer? oui/non: "))
            if rejouer == "oui":
                jeu_devinette() #le code recommence
            if rejouer == "non":
                exit() #si la personne ne veut plus jouer, l'ordinateur tue le code
                return (nombre_random)

jeu_devinette() #le code recommence