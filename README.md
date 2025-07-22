# CODEXINTERN-PYTHON-DEVELOPMENT-INTERNSHIP

This repository contains three projects completed as part of a data science internship. Each task demonstrates the use of core Python libraries for data analysis, machine learning, and interactive app development.

##  Tasks Overview

1. Task 1 – Data Analysis on Titanic Dataset using Pandas & Matplotlib  
2. Task 2 – House Price Prediction using California Housing Dataset  
3. Task 3 – Matrix Operations Tool using Streamlit & NumPy

---

## Task 1 – Titanic Data Analysis with Pandas and Matplotlib

Analyze the Titanic dataset to understand passenger survival patterns using basic statistics and visualizations.

Dataset: train.csv (Titanic Dataset)  
Source: https://www.kaggle.com/competitions/titanic/data

### Features

- Data cleaning: Handling missing values
- Statistical analysis: Mean age, fare, etc.
- Visualizations:
  - Survival count (bar chart)
  - Survival by gender
  - Age vs. Fare (scatter plot)
  - Heatmap of correlations
- Observations and interpretations from the visuals

Libraries used: pandas, matplotlib, seaborn

---

## Task 2 – House Price Prediction using California Housing Dataset

Build a regression model to predict median house values using the California Housing dataset available via scikit-learn.

Dataset: California Housing Dataset (via sklearn.datasets)

###  Features

- Load dataset using sklearn.datasets.fetch_california_housing
- Feature-target split (MedInc, HouseAge, AveRooms, etc.)
- Train-test split using scikit-learn
- Model building with Linear Regression
- Evaluation metrics:
  - Mean Squared Error (MSE)
  - R² Score
- Visualization of actual vs. predicted values

xample target: Median house value in California districts

Libraries used: pandas, numpy, matplotlib, scikit-learn

---

## Task 3 – Matrix Operations Tool using Streamlit and NumPy

A web-based matrix calculator that allows users to perform common matrix operations interactively using Streamlit.

File: matrix_tool_app.py  
Built with: Streamlit + NumPy

### Features

- Input matrices A and B through text boxes (space-separated values)
- Supported operations:
  - Addition (A + B)
  - Subtraction (A - B)
  - Multiplication (A × B)
  - Transpose (A or B)
  - Determinant (A or B)
- Input validation and error handling
- Real-time result display in Streamlit interface

### Conclusion
These tasks demonstrate essential data science skills:
- Task 1: Data exploration and visualization

- Task 2: Regression modeling and evaluation

- Task 3: Python GUI development using Streamlit
