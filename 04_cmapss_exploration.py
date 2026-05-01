import pandas as pd 
import numpy as np

#noms des colonnes d'après le readme
colonnes= ['moteur_id', 'cycle', 'op1', 'op2', 'op3', 
           's1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9',
           's10', 's11', 's12', 's13', 's14', 's15', 's16',
           's17', 's18', 's19', 's20', 's21']

#chargements des données 
df= pd.read_csv('data/train_FD001.txt', sep='\s+',
                header=None, names=colonnes,
                engine='python', on_bad_lines='skip')


df= df.dropna(axis=1, how='all') # supprime les colonnes vides 
#il y a toujours une colonne vide --> Regler ça plus tard 

print(df.columns.tolist())
print(f"Nombre de colonnes: {df.shape}")
print(df.head())

#Combien de moteurs différents?
print(f"Nombre de moteurs: {df['moteur_id'].nunique()}")


#combien de cycles par moteur en moy?
print(f"Nombre de cycles/moteur en moyenne: {df.groupby('moteur_id')['cycle'].max().describe()}")

#Calculer la RUL pour chaque ligne
cycle_max= df.groupby('moteur_id')['cycle'].transform('max')
df['RUL']= cycle_max - df['cycle']

print(df[['moteur_id', 'cycle', 'RUL']].head(10))

# temperature moyenne (s2) sur tout le dataset
print(f"Température moyenne s2: {df['s2'].mean()}")


#combien de lignes concernent le moteur 5? 
print(f"Cycles du moteur 5: {len(df[df['moteur_id']==5])}")

#Le cycle max atteint par le moteur 42?
##On filtre d'abord le moteur 42, puis on prend le max du cycle 
print(f"Cycle max moteur 42: {df[df['moteur_id']==42]['cycle'].max()}")

#les lignes où la RUL est inférieure 10 (moteurs en fin de vie)
print(f"Lignes où RUL < 10 : {df[df['RUL'] < 10]}")