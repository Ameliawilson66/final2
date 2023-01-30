#Amelia Wilson
import random

#on donne des caracteristiques au npc
class NPC:

    def __init__(self):
        #lancededes est le roule de 4 d6, l'addition des 3 valeurs supérieures
        self.force = lancededes()
        self.agilite = lancededes()
        self.constitution = lancededes()
        self.intelligence = lancededes()
        self.sagesse = lancededes()
        self.charisme = lancededes()
        #la classe d'armure est décidée par un d12
        self.classearmure = random.randint(1, 12)
        #le joueur décide ce qu'il y a dans les "   "
        self.nom = " "
        self.race = " "
        self.espèce = " "
        #les points de vie sont décidés par un d20
        self.pointsdevie = random.randint(0, 20)
        self.profession = " "

    def afficher_caracteristiques(self):
        print(self.force, self.agilite, self.constitution, self.intelligence, self.sagesse, self.charisme, self.classearmure, self.nom, self.race, self.espèce, self.pointsdevie, self.profession)

class Kobold(NPC):
    def __init__(self):
        super().__init__()
    def subir_dommages(self, paramètre1):
        #le monstre(Kobold) subit des dommages
        self.pointsdevie -= paramètre1

        return

class Hero(NPC):
    def __init__(self):
        super().__init__()
    def attaque(self, paramètre1 = Kobold):
        attaque = random.randint(1,20)
        #attaque critique, subit un d8 de dommages
        if attaque == 20:
            af = random.randint(1,8)
            paramètre1.subir_dommages(af)
        #attaque ratée, subit rien
        if attaque == 1:
            print("attaque ratée")

        if attaque >= 2 and attaque <= 19:
            #quand la classe d'armure du monstre(paramètre1) est inférieure au nombre roulé sur le d20, subit un d6 de dommages
            if self.classearmure < attaque:
                dommagesreg = random.randint(1,6)
                paramètre1.subir_dommages(dommagesreg)
            #quand le calsse d'armure de monstre(paramètre1) est supérieure au nombre roulé sur le d20, subit rien
            if self.classearmure > attaque:
                print("attaque ratée")
        return

    #les dommages du héro
    def subir_dommages(self, paramètre2):
        return

def lancededes():
    de1 = random.randint(1, 6)
    de2 = random.randint(1, 6)
    de3 = random.randint(1, 6)
    de4 = random.randint(1, 6)
#prendre seulement les 3 dés des 4 roulés qui ont la plus grande valeure
    if de1 < de2 and de1<de3 and de1<de4:
        return de2 + de3 + de4
    if de2<de1 and de2<de3 and de2<de4:
        return de1 + de3 + de4
    if de3<de1 and de3<de2 and de3<de4:
        return de1 + de2 + de4
    if de4<de1 and de4<de2 and de4<de3:
        return de1 + de2 + de3