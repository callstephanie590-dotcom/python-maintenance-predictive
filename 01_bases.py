
rul = 45 # Remaining Useful Life d'un moteur en cycles

if rul > 100:
    print("Moteur en bon état")
elif rul > 30:
    print("Moteur à surveiller ")
else:
    print("Intervention urgente ")

moteurs = [120, 45, 8, 200, 27]

for rul in moteurs:
    if rul > 100:
        print(f"RUL {rul} — Moteur en bon état ")
    elif rul > 30:
        print(f"RUL {rul} — Moteur à surveiller ")
    else:
        print(f"RUL {rul} — Intervention urgente ")

#EXO 1

bon_etat=0
a_surveiller=0
intervention_urgente=0 

for rul in moteurs: 
    if rul>100: 
        bon_etat+=1
    elif rul>30:
        a_surveiller+=1
    else:
        intervention_urgente+=1
    print("---Résumé flotte")
    print(f"Bon état:{bon_etat} moteurs")
    print(f"A surveiller: {a_surveiller} moteurs")
    print(f"Urgent: {intervention_urgente} moteurs")

#EXO 2
températures= [450, 523, 612, 489, 701, 634, 478, 590]
température_normale=0
température_elevée=0
temperature_critique=0
moy_température=sum(températures)/len(températures)
for rul in températures:
    if rul>650:
        temperature_critique+=1
        print(f"RUL{rul} - Température critique")
    elif rul>500:
        température_elevée+=1
        print(f"RUL{rul} - Température élevée")
    else:
        température_normale+=1
        print(f"RUL{rul} - Température normale")

print("---Résumé Températures")
print(f"Température normale: {température_normale} relevés")
print(f"Température élevée: {température_elevée} relevés")
print(f"Température critique: {temperature_critique} relevés")
print(f"Températue moyenne: {moy_température:.1f}°C")

#Exo bonus

capteurs=[12, 7, 18, 3, 15, 9, 21, 6]
moy_capteurs=sum(capteurs)/len(capteurs)
superieur_moy=0
inferieur_moy=0
max= capteurs[0] #on part du premier element de la liste dont le decompte commence à 0 
min= capteurs[0]

for rul in capteurs:
    if rul>max:
        max=rul
    if rul<min:
        min=rul

print(f"La valeur maximale des capteurs est {max}")
print(f"La valeur minimale des capteurs est {min}")

for rul in capteurs: 
    if rul>moy_capteurs:
        superieur_moy+=1
    else:
        inferieur_moy+=1
    
print(f"Moyenne des capteurs: {moy_capteurs:.1f}")
print(f"Capteurs superieurs à la moyenne: {superieur_moy} capteurs")
print(f"Capteurs inferieurs à la moyenne: {inferieur_moy} capteurs ")

#FONCTIONS
def évaluer_moteur(rul):
    if rul > 100:
        return "bon état"
    elif rul > 30:
        return "à surveiller"
    else:
        return "Intervention urgente"
moteurs = [120, 45, 8, 200, 27]
for rul in moteurs:
    état = évaluer_moteur(rul)
    print(f"RUL {rul} — Moteur en {état}")  

#EXO 3
def evaluer_température(rul):
    if rul>650:
        return "Température critique"
    elif rul>500:
        return "Température élevée"
    else:
        return "Température normale"

températures= [450, 523, 612, 489, 701, 634, 478, 590]
for rul in températures:
    état2 = evaluer_température(rul)
    print(f"La température est de {rul}°C — {état2}")



#dictionnaire

def evaluer_moteur(rul):
    if rul > 100:
        return "bon état"
    elif rul > 30:
        return "à surveiller"
    else:
        return "Intervention urgente"

def evaluer_température(rul):
    if rul>650:
        return "Température critique"
    elif rul>500:
        return "Température élevée"
    else:
        return "Température normale"

flotte= [
    {"moteur": 1, "rul": 120, "temp": 450},
    {"moteur": 2, "rul": 45, "temp": 523},
    {"moteur": 3, "rul": 8, "temp": 701},
    {"moteur": 4, "rul": 200, "temp": 489},
]
for m in flotte:
    etat_rul = evaluer_moteur(m["rul"])
    etat_temp = evaluer_température(m["temp"])
    print(f"Moteur {m['moteur']} —  {etat_rul} - {etat_temp}")


#EXO 4

def diagnostic_moteur(rul,temperature):
    if rul<30 and temperature>650:
        return "ARRET IMMEDIAT"
    elif rul<30 or temperature>650:
        return "VERFICATION URGENTE"
    else:
        return "Nominal"

flotte2= [
    {"moteur": 1, "rul":8, "temperature": 701},
    {"moteur": 2, "rul": 8, "temperature": 450},
    {"moteur": 3, "rul": 120, "temperature": 701},
    {"moteur": 4, "rul": 120, "temperature": 450},
]

for moteur in flotte2:
    etat_rul2=diagnostic_moteur(moteur["rul"], moteur["temperature"])
    print(f"Moteur {moteur['moteur']} _ {etat_rul2}")


#exemple listes

capteurs=[12, 7, 18, 3, 15]

print(capteurs[0]) #affiche le premier element de la liste
print(capteurs[-1]) #affiche le dernier element de la liste

capteurs.append(42) #ajoute un element à la fin de la liste
capteurs.remove(7) #supprime l'element 7 de la liste

print(capteurs[1:4]) #affiche les elements d'indice 1 à 3 (4 n'est pas inclus)
print(capteurs[:3]) #affiche les 3 premiers elements de la liste
print(capteurs[2:]) #affiche les elements à partir de l'indice 2 (du troisième) jusqu'à la fin de la liste

#liste double 

capteurs=[12, 7, 18, 3, 15, 9, 21, 6]

doubles = [c*2 for c in capteurs] #crée une nouvelle liste avec les éléments de capteurs multipliés par 2
print(doubles) 

carré= [c**2 for c in capteurs] #crée une nouvelle liste avec les éléments de capteurs élevés au carré
print(carré)

pair= [c for c in capteurs if c % 2 == 0] #crée une nouvelle liste avec les éléments pairs 
print(pair)