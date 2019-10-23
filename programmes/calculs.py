from heures import *


# |
# |  FONCTIONNE MAIS PAS PARFAIT MANQUE UNE CONDITION SI IL RESTE MOINS DE 15 KM APRES LA DERNIERE PAUSE
# V

def tempsDeRoute(dist):
    Durée = 0
    NBpause = dist / 168
    NBpause = int(NBpause)
    Durée = Durée + (NBpause * 0.25) + (NBpause * 2)
    restant = dist % 168
    restant -= 15 # Le camion va mettre environ 15km a accélerer et ralentir   
    Durée += 0.3
    Durée += restant / 90 
    return DecimalToHeure(Durée)

