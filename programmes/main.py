from heures import *
from calculs import *
from pick import *
from trajets import *


depart = pick(villes,'Choisissez votre ville de départ')
arrive = pick(villes,"Choisissez votre ville d'arrive (différente de la ville de départ)")
trajet = depart[0] + '-' + arrive[0]
dist = distTrajets[trajet]

print('Il fera',depart[0],'---->',arrive[0],'en',tempsDeRoute(dist))
