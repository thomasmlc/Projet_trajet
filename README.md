# Projet_trajet
 
## Prérequis

### Librairie pick 

Il faudra d'abors installer la librairie Python Pick :
```
pip install pick
pip install windows-curses
```

## Lancement du programme 

### Lancer le fichier main.py
En lançant main.py vous allez avoir le choix entre une ville de départ et une d'arrivée.  
Pour la selectionner déplacez-vous à l'aide des fléches et validez avec la touche entrée .

Ceci affichera votre trajet ainsi que le temps de route que le camion va effectuer.   

### Calcul manquant   
Mon programme ne calcul pas le temps de trajet exact s'il reste moins de 15km après la dérnière pause.