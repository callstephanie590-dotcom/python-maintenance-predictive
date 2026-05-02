import pandas as pd
import numpy as np 

#colonnes (readme)
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


#Calculer la RUL pour chaque ligne
cycle_max= df.groupby('moteur_id')['cycle'].transform('max')
df['RUL']= cycle_max - df['cycle']


print(f"Nombre de colonnes: {df.shape}")

#Capteurs utiles (ceux qui dérivent, on retire les constants)
capteurs_utiles= ['s2', 's3', 's4', 's7', 's8', 's9',
                  's11', 's12', 's13', 's14', 's15',
           's17', 's20', 's21']

#Moyenne glissante sur 5 cycles pour lisser le bruit
for capteur in capteurs_utiles: 
    df[f'{capteur}_mean5']= df.groupby('moteur_id')[capteur].transform(
        lambda x: x.rolling(window=5, min_periods=1).mean()
    )

print(df[['moteur_id', 'cycle', 's2', 's2_mean5', ]].head(10))
print(f"Nouvelles dimensions: {df.shape}")


from sklearn.preprocessing import MinMaxScaler

#Colonnes à normaliser 
features= [f'{c}_mean5' for c in capteurs_utiles]

#Normalisation entre 0 et 1
scaler= MinMaxScaler()
df[features]= scaler.fit_transform(df[features])

print(df[features].describe().round(2))

#X=les features (capteurs lissés et normalisés)
#y=la cible (RUL à prédire)
X= df[features]
y=df['RUL']

print(f"X : {X.shape}")
print(f"y : {y.shape}")
print(f"Exemple de RUL à prédire: {y.head().values}")





