import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#chargement des données (les memes que dans le code précédent)
colonnes= ['moteur_id', 'cycle', 'op1', 'op2', 'op3', 
           's1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9',
           's10', 's11', 's12', 's13', 's14', 's15', 's16',
           's17', 's18', 's19', 's20', 's21']

df= pd.read_csv('data/train_FD001.txt', sep='\s+',
                header=None, names=colonnes,
                engine='python', on_bad_lines='skip')


df= df.dropna(axis=1, how='all') 

cycle_max= df.groupby('moteur_id')['cycle'].transform('max')
df['RUL']= cycle_max - df['cycle']

#1er graph: évolution du capteur s2 pour le moteur 1
moteur1= df[df['moteur_id']==1]

plt.figure(figsize=(10,4))  #dimensions de la figure
plt.plot(moteur1['cycle'], moteur1['s2'])
plt.xlabel('Cycle')  #axe des abscisses
plt.ylabel('s2 - Température')  #axe des ordonnées 
plt.title('Evolution du capteur s2 - Moteur 1') #titre 
plt.grid(True)
plt.savefig('img_capteur_s2.png', dpi=150, bbox_inches='tight') 
plt.show()


#GRAPHE 2: Comparaison de 4 capteurs sur le moteur 1
fig, axes= plt.subplots(2, 2, figsize=(12, 8))

capteurs= ['s2', 's3', 's4', 's7']

for i, capteur in enumerate(capteurs):
    ax = axes[i//2][i%2]
    ax.plot(moteur1['cycle'], moteur1[capteur])
    ax.set_title(f'Capteur {capteur}')
    ax.set_xlabel('Cycle')
    ax.grid(True)

plt.suptitle('Evolution des capteurs - Moteur 1')
plt.tight_layout()
plt.savefig('img_capteurs_multiples.png', dpi=150, bbox_inches='tight')
plt.show()


#graphe 3 :RUL en fonction du cycle(tous les moteurs superposés)
plt.figure(figsize=(10,5))

for moteur_id in df['moteur_id'].unique()[:20]: #on prend 20 moteurs
    m = df[df['moteur_id']== moteur_id]
    plt.plot(m['cycle'], m['RUL'], alpha=0.3, color='blue')  #alpha=0,3 rend les courbes semi transparentes pour voir les superpositions

plt.xlabel('Cycle')
plt.ylabel('RUL')
plt.title("RUL en fonction du cycle - 20 moteurs")
plt.grid(True)
plt.savefig('img_rul_20moteurs.png', dpi=150, bbox_inches='tight')
plt.show()


#graphe 4: distributions des rul
plt.figure(figsize=(8,4))
plt.hist(df[df['cycle'] == 1]['RUL'], bins=20, color='steelblue', edgecolor='black') # on selectionne le 1er cycle de chaque moteur (RUL max)
plt.xlabel('RUL initiale (cycles)')
plt.ylabel('Nombres de moteurs')
plt.title('Distribution de la durée de vie des moteurs')
plt.grid(True)
plt.savefig('img_distribution_rul.png', dpi=150, bbox_inches='tight')
plt.show()






