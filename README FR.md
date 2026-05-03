# Maintenance Predictive — Dataset NASA CMAPSS

Prédiction de la durée de vie résiduelle (RUL) de moteurs de turboreacteurs par machine learning — des données capteurs brutes à un dashboard de maintenance opérationnel.

# Présentation

Ce projet construit un pipeline complet de maintenance prédICTive sur le dataset NASA CMAPSS — référence académique internationale en surveillance de santé des équipements industriels (PHM).

L'objectif : prédire combien de cycles opérationnels restent avant la panne d'un moteur, pour permettre aux équipes de maintenance d'intervenir avant la défaillance.

Ce projet simule un cas d'usage réel de maintenance conditionnelle utilisé dans l'aeronautique pour optimiser la disponibilité des équipements et réduire les coûts d'immobilisation non planifiée.

# Dataset

NASA CMAPSS — sous-ensemble FD001

<table><tr><td>Caractéristique</td><td>Valeur</td></tr><tr><td>Lignes totales</td><td>20 631 cycles</td></tr><tr><td>Moteurs</td><td>100</td></tr><tr><td>Capeurs</td><td>21 (14 informatifs)</td></tr><tr><td>Durée de vie moyenne</td><td>206 cycles</td></tr><tr><td>Min / Max</td><td>128 / 362 cycles</td></tr></table>

# Pipeline

<table><tr><td>Etape</td><td>Description</td><td>Statut</td></tr><tr><td>Exploration</td><td>Chargement CMAPSS, analyse capteurs, calcul RUL</td><td>Terminé</td></tr><tr><td>Visualisation</td><td>Dérive des capteurs, distribution RUL, vue flotte</td><td>Terminé</td></tr><tr><td>Feature Engineering</td><td>Moyenne glissante (window=5), normalisation MinMax</td><td>Terminé</td></tr><tr><td>Random Forest</td><td>Modèle de référence — MAE 22,U cycles</td><td>Terminé</td></tr><tr><td>Gradient Boosting</td><td>Modèle amélioré — cible MAE &lt; 20 cycles</td><td>En cours</td></tr><tr><td>Dashboard Streamlit</td><td>Interface interactive vue moteur et vue flotte</td><td>Prévu</td></tr><tr><td>Déploiement</td><td>Streamlit Cloud + documentation complète</td><td>Prévu</td></tr></table>

# Résultats — Random Forest (baseline)

<table><tr><td>Métrique</td><td>Valeur</td><td>Interprétable</td></tr><tr><td>RMSE</td><td>33,6 cycles</td><td>Erreur quadratique</td></tr><tr><td>MAE</td><td>22,9 cycles</td><td>Écart moyen prédiction / réalité</td></tr><tr><td>Split Train / Test</td><td>80% / 20%</td><td>16 504 / 4 127 observations</td></tr></table>

Le modele est particulièrement précis pour les faibles valeurs de RUL (0-100 cycles) — la zone la plus critique pour les décisions de maintenance.

# Stack Technique

- Python 3.10   
- Pandas / NumPy — manipulation des données   
- Matplotlib — visualisation   
Scikit-learn - machine learning   
- Streamlit—dashboard (àvenir)

# Structure du projet

python-maintenance-predictive/

data/

train_FD001.txt test_FD001.txt RUL_FD001.txt

01bases.py   
02 numpy.py   
03pandas.py   
04cmapss Exploration.py   
05visualization.py   
06 feature engineering.py   
07machine_learning.py   
docs/

— rapport_intermédiaire_cmapss.pdf

README.md

# Comment exécuter ?

git clone https://github.com/callstephanie590-dotcom/python-maintenance-predictive  
cd python-maintenance-predictive  
pip install pandas numpy matplotlib scikit-learn  
python 04_cmapss Exploration.py  
python 05VISUALISATION.py  
python 07 MACHINE_LEARNING.py

# Auteure

Stéphanie CALLEGARI Étudiante Ingénieure — Systèmes d'Information & Génie Industriel  
EPF École d'Ingénieurs, Cachan

Recherche activement une alternance — September 2026

# Licence

Ce projet utilise le jeu de données NASA CMAPSS, disponible publiquement à des fins de recherche et d'enseignement.
