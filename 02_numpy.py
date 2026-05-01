import numpy as np

#créer un array
capteurs= np.array([12, 7, 18, 3, 9, 21, 6])

print(capteurs)
print(type(capteurs))

#Opérations instantanées sur tout le tableau
print(np.mean(capteurs))
print(np.max(capteurs))
print(np.min(capteurs))
print(np.std(capteurs))

#Opérations vectorisées
print(capteurs*2) #multiplie chaque élément par 2
print(capteurs**2) #met au carré chaque élément au carré
print(capteurs>10) #renvoie un tableau de booléens indiquant si chaque élément est supérieur à 10

#filtrage 
print(capteurs[capteurs>10]) #affiche les éléments du tableau qui sont > à 10

#un array 2D - imagine 3 moteurs avec 4 capteurs chacun
donnees= np.array([
    [450, 12, 0.9, 520],
    [480, 15, 0.85, 505],
    [612, 21, 0.7, 490]
])

print(donnees.shape) #dimensions du tableau (3 lignes, 4 colonnes)
print(donnees[0]) #première ligne (données du moteur 1)
print(donnees[:, 0]) #première colonne (vitesse de rotation de chaque moteur)
print(donnees[:, 0].mean()) #Température moyenne de la flotte 


#EXO1

##Valueur moy de chaque capteur sur toute la flotte (colonnes)
print(np.mean(donnees, axis=0)) #moyenne de chaque colonne (capteur)

moy_capteurs=np.mean(donnees, axis=0) #pour y voir plus clair
for i, moy in enumerate(moy_capteurs):
    print(f"Capteur {i+1}: {moy:.2f}")

##etat moy de chaque moteur (lignes)
print(np.mean(donnees, axis=1)) #moyenne de chaque ligne (moteur)

moy_moteurs= np.mean(donnees, axis=1)
for i, moy in enumerate(moy_moteurs):
    print(f"Moteurs {i+1}: {moy:.2f}")


