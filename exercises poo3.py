#Amelia Wilson
import random

class NPC:

    def __init__(self):

        self.force = lancededes()
        self.agilite = lancededes()
        self.constitution = lancededes()
        self.intelligence = lancededes()
        self.sagesse = lancededes()
        self.charisme = lancededes()

        self.classearmure = random.randint(1, 12)
        self.nom = " "
        self.race = " "
        self.espèce = " "
        self.pointsdevie = random.randint(0, 20)
        self.profession = " "

        print(self)

class Kobold(NPC):
    def __init__(self):
        super().__init__()
    def subir_dommages(self, paramètre1):
        self.pointsdevie -= paramètre1
        self.pointsdevie -= dommagesreg

        return

class Hero(NPC):
    def attaque(self, paramètre1 = Kobold):
        attaque = random.randint(1,20)
        if attaque == 20:
            af = random.randint(1,8)
            paramètre1.subir_dommages(af)
        if attaque == 1:
            rien = 0
            paramètre1.subir_dommages(rien)

        if attaque in range (2,19):
            if self.classearmure < attaque:
                dommagesreg = random.randint(1,6)
                paramètre1.subir_dommages(dommagesreg)
            if self.classearmure > attaque:
                rien = 0
                paramètre1.subir_dommages(rien)
        return

    def subir_dommages(self, paramètre2):

def lancededes():
    de1 = random.randint(1, 6)
    de2 = random.randint(1, 6)
    de3 = random.randint(1, 6)
    de4 = random.randint(1, 6)

    if de1 < de2 and de1<de3 and de1<de4:
        return de2 + de3 + de4
    if de2<de1 and de2<de3 and de2<de4:
        return de1 + de3 + de4
    if de3<de1 and de3<de2 and de3<de4:
        return de1 + de2 + de4
    if de4<de1 and de4<de2 and de4<de3:
        return de1 + de2 + de3