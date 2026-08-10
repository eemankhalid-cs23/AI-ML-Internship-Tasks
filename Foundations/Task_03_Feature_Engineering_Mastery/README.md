# Task 03 — Feature Engineering Mastery

## Overview

This task focuses on applying feature engineering and feature selection techniques to improve house price prediction using the **House Prices — Advanced Regression Techniques** dataset.

## Objectives

- Create meaningful features from existing data.
- Transform categorical variables using one-hot encoding.
- Apply feature selection techniques to identify useful predictors.
- Compare model performance before and after feature selection.

## Key Work

- Data exploration and preprocessing
- Feature creation and transformation
- One-hot encoding
- Feature selection
- Baseline and feature-selected model evaluation

## Results

| Metric | Baseline | Feature-Selected |
|---|---:|---:|
| Features | 267 | 192 |
| MAE | 17,855.86 | **17,448.28** |
| RMSE | 30,036.68 | **29,588.89** |
| R² | 0.8824 | **0.8859** |

## Conclusion

Feature selection reduced the number of features from **267 to 192** while improving model performance. The final MAE of **17,448.28** achieved the target of keeping MAE below **18,000**.
