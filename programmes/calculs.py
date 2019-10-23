from heures import *

""" DeuxHeuresRoute = 168
dist = 582
DistManque = 582 % 168
NBpause = 582 / 168
NBpause = int(NBpause) """

def tempsDeRoute(dist):
    Durée = 0
    NBpause = dist / 168
    NBpause = int(NBpause)
    Durée = Durée + (NBpause * 0.25) + (NBpause * 2)
    restant = dist % 168
    restant -= 15
    Durée += restant / 90 
    print ('Il va mettre',DecimalToHeure(Durée),'et faire',NBpause, 'pauses.')
    
# le modulo c'est fou 
# en gros division par 174 donne le nombre de pauses 
# et modulo donne la distance réstante a calculer
