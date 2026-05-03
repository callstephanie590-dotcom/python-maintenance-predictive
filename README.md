# Predictive Maintenance — NASA CMAPSS Turbofan Engine Dataset

Predicting the Remaining Useful Life (RUL) of aircraft turbofan engines using machine learning — from raw sensor data to an operational maintenance dashboard.

# Project Overview

This project builds a complete predictive maintenance pipeline on the NASA CMAPSS dataset — a reference benchmark in industrial health monitoring (PHM).

The goal: predict how many operational cycles remain before a turbofan engine fails, enabling maintenance teams to intervene before breakdown rather than after.

This simulates a real-world use case in aeronautics — conditional maintenance systems used to optimize equipment availability and reduce unplanned downtime costs.

# Dataset

NASA CMAPSS — FD001 subset   

<table><tr><td>Feature</td><td>Value</td></tr><tr><td>Total rows</td><td>20,631 cycles</td></tr><tr><td>Engines</td><td>100</td></tr><tr><td>Sensors</td><td>21 (14 informative)</td></tr><tr><td>Average lifetime</td><td>206 cycles</td></tr><tr><td>Min / Max lifetime</td><td>128 / 362 cycles</td></tr></table>

Each row represents one operational cycle of one engine. Engines degrade progressively from healthy state to failure — no intermediate maintenance.

# Pipeline

Raw data $\rightarrow$ Exploration $\rightarrow$ Feature Engineering $\rightarrow$ ML Model $\rightarrow$ Dashboard

<table><tr><td>Step</td><td>Description</td><td>Status</td></tr><tr><td>Data Loading &amp; Exploration</td><td>CMAPSS loading, sensor analysis, RUL calculation</td><td>Done</td></tr><tr><td>Visualization</td><td>Sensor drift, RUL distribution, fleet overview</td><td>Done</td></tr><tr><td>Feature Engineering</td><td>Rolling mean (window=5), MinMax normalization</td><td>Done</td></tr><tr><td>Random Forest</td><td>Baseline model — MAE 22.U cycles</td><td>Done</td></tr><tr><td>Gradient Boosting</td><td>Improved model — target MAE &lt; 20 cycles</td><td>In progress</td></tr><tr><td>Streamlit Dashboard</td><td>Interactive fleet monitoring interface</td><td>Planned</td></tr><tr><td>Deployment</td><td>Streamlit Cloud + full documentation</td><td>Planned</td></tr></table>

# Results — Random Forest (baseline)

<table><tr><td>Metric</td><td>Value</td><td>Interpretation</td></tr><tr><td>RMSE</td><td>33.6 cycles</td><td>Quadratic error — penalizes large errors</td></tr><tr><td>MAE</td><td>22.9 cycles</td><td>Average prediction error</td></tr><tr><td>Train / Test split</td><td>80% / 20%</td><td>16,504 / 4,127 observations</td></tr></table>

The model is particularly accurate for low RUL values (0-100 cycles) — the most critical zone for maintenance decisions. For high RUL values, the model tends to underestimate — a conservative bias that is acceptable and even desirable in safety-critical industrial contexts.

# Tech Stack

- Python 3.10   
- Pandas / NumPy — data manipulation   
- Matplotlib — visualization   
- Scikit-learn — machine learning (Random Forest, MinMaxScaler)   
- Streamlit — dashboard (coming soon)

# Project Structure

```batch
python-maintenance-predictive/  
data/  
train_FD001.txt  
test_FD001.txt  
RUL_FD001.txt  
01bases.py  
02numpy.py  
03pandas.py  
04cmapss Exploration.py  
05visualisation.py  
06featureengineering.py  
07machine_learning.py  
docs/  
rapport_intermediaire_cmapss.pdf  
README.md 
```

# How to Run

git clone https://github.com/callstephanie590-dotcom/python-maintenance-predictiv cd python-maintenance-predictive

pip install pandas numpy matplotlib scikit-learn python

04_cmapss_exploration.py

python 05VISUALISATION.py python

07-machine_learning.py

# Author

Stéphanie CALLEGARI Engineering Student — Information Systems & Industrial Engineering EPF École d'Ingénieurs, Cachan

Actively seeking a work-study alternance contract — September 2026

# License

This project uses the NASA CMAPSS dataset, publicly available for research and educational purposes.
