# Amelia Wilson 401
# tp2

#exercice a
print('hello world!')

#exercice b
x = input('entrez votre nom: ')
print('hello, ' + x)

#exercice c
nombre = int(input('combiende rangées voulez vous: '))
for i in range(nombre + 1, 0,-1):
    print('*'*i)

#jeu de devinette
import random

def jeu_devinette(): #identifier la variable
    nombre_random = random.randint(0, 1000)
    print('jai choisit un nombre entre 0 et 1000.')
    essai = int(input('nombre: '))
    nb_essai = 0

    while essai != nombre_random:
        nb_essai += 1

        if essai < nombre_random:
            essai = int(input("le nombre est plus grand: ")) #le nombre deviné est plus petit que le nombre choisit

        if essai > nombre_random:
            essai = int(input("le nombre est plus petit: ")) #le nombre deviné est plus grand que le nombre choisit

        if essai == nombre_random:
            print("bravo! vous avez devinez le bon nombre en " + str(nb_essai) + " essais.")
            rejouer = str(input("voulez-vous rejouer? oui/non"))
            if rejouer == "oui":
                jeu_devinette()
            if rejouer == "non":
                exit()
                return (nombre_random) #le jeu recommence


jeu_devinette()