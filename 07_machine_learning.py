import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#colonnes
colonnes= ['moteur_id', 'cycle', 'op1', 'op2', 'op3', 
           's1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9',
           's10', 's11', 's12', 's13', 's14', 's15', 's16',
           's17', 's18', 's19', 's20', 's21']

#données
df= pd.read_csv('data/train_FD001.txt', sep='\s+', header=None, names=colonnes, 
                engine='python', on_bad_lines='skip')

df.dropna(axis=1, how='all')


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


from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error

# Séparation train/test (80% entraînement, 20% test)
X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.2, random_state=42
)

print(f"Train : {X_train.shape} | Test : {X_test.shape}")

# Entraînement du modèle
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Évaluation
y_pred = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
mae = mean_absolute_error(y_test, y_pred)

print(f"RMSE : {rmse:.1f} cycles")
print(f"MAE : {mae:.1f} cycles")

import matplotlib.pyplot as plt

plt.figure(figsize=(8,8))
plt.scatter(y_test, y_pred, alpha=0.3, color='steelblue')
plt.plot([0, 400], [0, 400], 'r--') #ligne parfaite
plt.xlabel('RUL réelle')
plt.ylabel('RUL prédite')
plt.title('Random Forest - Prédiction vs Réalité')
plt.grid(True)
plt.show()