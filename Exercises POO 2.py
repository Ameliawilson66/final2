#Amelia Wilson
import random

a = random.randint(1, 6)
x = random.randint(1, 6)
y = random.randint(1, 6)
z = random.randint(1, 6)

class NPC:

    def __init__(self):

        self.force = lancededes()
        #choisir les 3 plus élevés(?)
        self.agilite = lancededes()
        self.constitution = lancededes()
        self.intelligence = lancededes()
        self.sagesse = lancededes()
        self.charisme = lancededes()

        self.classearmure = random.randint(1, 12)
        self.nom = " "
        self.pointsdevie = random.randint(0, 20)
        self.profession = " "

    class kobold:


def lancededes():
    if x > y:
        premier_chiffre_a_garder = x
        if y > z:
            deuxieme_chiffre_a_garder = y
            if z > a:
                troisiemechiffreagarder = z
            elif a > z:
                troisiemecvhiffreagarder = a