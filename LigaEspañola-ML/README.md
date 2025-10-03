# Spanish League Match Prediction (2024/25)

This project applies **Machine Learning** techniques to predict match outcomes for the Spanish League (LaLiga) season 2024/25. Data is retrieved from [football-data.co.uk](https://www.football-data.co.uk).

## Overview
- Load historical match data from the ongoing season.
- Apply **feature engineering**:
  - Recent team form
  - Goal difference
  - Head-to-head history
- Train classification models:
  - Random Forest
  - XGBoost with Grid Search
- Predict future matches with class probabilities.

## Repository Structure
"""
mermaid
graph TD
    A[LigaEspanola-ML]
    A --> B[notebooks]
    B --> B1[ML_LigaEspanola.ipynb]
    A --> C[outputs]
    C --> C1[confusion_matrix.png]
    C --> C2[xgb_model.pkl]
    A --> D[requirements.txt]
    A --> E[README.md]
"""

## Results
- Random Forest: ~XX% accuracy  
- XGBoost (optimized): ~YY% accuracy  

Example of predicted probabilities for upcoming matches:
"""
HomeTeam   AwayTeam   Prob_Home   Prob_Draw   Prob_Away
Sevilla    Barcelona     0.32        0.28        0.40
Getafe     Barcelona     0.21        0.25        0.54
"""

## Installation
Clone the repository and install dependencies:
"""
git clone https://github.com/yourusername/LigaEspanola-ML.git
cd LigaEspanola-ML
pip install -r requirements.txt
"""

## Usage
Open the notebook with Jupyter:
"""
jupyter notebook notebooks/ML_LigaEspanola.ipynb
"""

## Future Improvements
- Time-series validation with `TimeSeriesSplit`.
- Additional evaluation metrics: F1-score, Log Loss, Brier Score.
- More advanced features: win streaks, home advantage, matchday effects.

## Author
- Name: Andres Contreras  
- Year: 2025  
- Data Source: [football-data.co.uk](https://www.football-data.co.uk)
