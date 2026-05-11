# House Price Prediction - Kaggle Competition

## Project Overview

This project predicts house sale prices using machine learning techniques on the Kaggle House Prices dataset.

The goal is to build a regression model that can accurately estimate house prices based on features such as:
- house area
- overall quality
- construction year
- number of rooms
- bathrooms
- floor size

This project was built using Python, Scikit-learn, and XGBoost.

---

## Kaggle Competition

Competition:
House Prices - Advanced Regression Techniques

Competition Link:
https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques

---

## Dataset Information

Dataset files used:
- train.csv
- test.csv

Target Variable:
- SalePrice

Important features used:
- LotArea
- OverallQual
- YearBuilt
- 1stFlrSF
- 2ndFlrSF
- FullBath
- BedroomAbvGr
- TotRmsAbvGrd

The dataset contains:
- numerical features
- missing values
- real-world housing data

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- VS Code
- Git & GitHub

---

## Machine Learning Models Used

### 1. Random Forest Regressor
Used as the baseline machine learning model.

### 2. XGBoost Regressor
Used to improve prediction performance and leaderboard score.

Techniques used:
- missing value handling
- numerical feature selection
- gradient boosting

---

## Model Performance

### Random Forest Model
Kaggle Public Score:
0.16441

### XGBoost Model
Kaggle Public Score:
0.14334

The XGBoost model significantly improved prediction accuracy.

---

## Project Workflow

1. Data Loading
2. Data Exploration
3. Missing Value Handling
4. Feature Selection
5. Model Training
6. Model Evaluation
7. Kaggle Submission
8. Score Improvement

---

## Project Structure

house-price-prediction-kaggle/
│
├── data/
│   ├── train.csv
│   └── test.csv
│
├── main.py
├── requirements.txt
├── submission.csv
├── README.md
└── .gitignore

---

## Installation

Clone the repository:

```bash
git clone https://github.com/chandupatel-ai/house-price-prediction-kaggle.git
