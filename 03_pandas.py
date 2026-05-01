import pandas as pd
import numpy as np

#creer un DataFrame(tableau de données central de pandas)
data= {
    "moteur": [1, 2, 3, 4],
    "rul" : [120, 45, 8, 200],
    "temperature": [450, 523, 701, 489],
    "pression": [0.9, 0.85, 0.7, 0.95]
}

df = pd.DataFrame(data)
print(df)
print()
print(df.shape)
print(df.dtypes)

#accéder à une colonne
print(df["rul"])

#accéder à plusieurs colonne
print(df[["moteur", "temperature"]])

#filtrer les lignes
print(df[df["rul"]>50])

# Statistiques descriptives en une ligne 
print(df.describe())

#acceder à une valeur précise 
print(df["temperature"].mean())
print(df["rul"].max())
print(df["rul"].min())
