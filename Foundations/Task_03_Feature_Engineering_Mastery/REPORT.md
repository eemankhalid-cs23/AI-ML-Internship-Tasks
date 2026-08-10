# Task 03 — Feature Engineering Mastery Report

## 1. Introduction

This task focuses on improving a house price prediction model through feature engineering and feature selection. The **House Prices — Advanced Regression Techniques** dataset was used because it contains a wide range of property-related attributes that can be transformed into more informative features for regression.

The main goal was to improve prediction accuracy while reducing unnecessary features. The required target was to achieve a Mean Absolute Error (MAE) below **$18,000**.

## 2. Dataset Description

The dataset contains **1,460 residential property records** with information about different aspects of each house, including:

- Property size and area
- Overall quality and condition
- Construction and remodeling
- Basement features
- Garage features
- Rooms and bathrooms
- Neighborhood and location characteristics
- Exterior and structural information
- Sale-related attributes

The prediction target was **`SalePrice`**, representing the final sale price of each property.

The dataset initially contained **86 columns** after the relevant data preparation stage.

## 3. Data Preparation

The dataset was loaded and examined to understand its structure, available variables, and data types before applying feature engineering.

Categorical variables were converted into numerical representations using **one-hot encoding**. This created separate binary columns for different categories and increased the feature space from the original prepared dataset to **268 encoded columns**.

The resulting feature matrix was prepared for machine learning model training.

## 4. Feature Engineering

New features were created by combining related variables to represent useful property characteristics more directly.

Important engineered features included:

### HouseAge
Represents the age of the property based on its construction year and the relevant sale year.

### TotalBathrooms
Combines the available full and half bathroom information into a more representative measure of total bathroom availability.

### TotalPorchSF
Combines different porch and outdoor living area measurements into one feature representing total porch area.

### TotalSF
Combines relevant floor and basement area measurements to represent the overall usable property space.

These transformations were designed to provide the model with more meaningful information than relying only on separate raw variables.

## 5. Categorical Encoding

Categorical variables such as zoning, neighborhood, exterior characteristics, and other property categories cannot be directly used by most regression algorithms in their original text form.

Therefore, **one-hot encoding** was applied.

For example, a categorical variable with multiple possible values was converted into multiple binary features. This allowed the model to use categorical information without assigning an artificial numerical order to the categories.

After encoding, the feature matrix contained **268 features**.

## 6. Feature Selection

Although the encoded dataset contained many features, not all features were equally useful for predicting `SalePrice`.

Feature selection was therefore applied to identify the most informative predictors and reduce unnecessary dimensionality.

The initial model used **267 features** after the final feature preparation stage.

After feature selection, the number of features was reduced to:

**192 features**

This reduced the feature space by **75 features** while retaining the features selected as useful for prediction.

## 7. Baseline Model

A baseline regression model was trained using the complete prepared feature set.

The baseline performance was:

| Metric | Baseline |
|---|---:|
| Number of Features | 267 |
| MAE | 17,855.86 |
| RMSE | 30,036.68 |
| R² | 0.8824 |

The baseline MAE was already below the required $18,000 target, but feature selection was evaluated to determine whether performance could be improved while using fewer features.

## 8. Feature-Selected Model

A second model was trained using the **192 selected features**.

The resulting performance was:

| Metric | Feature-Selected |
|---|---:|
| Number of Features | 192 |
| MAE | 17,448.28 |
| RMSE | 29,588.89 |
| R² | 0.8859 |

## 9. Performance Comparison

| Metric | Baseline | Feature-Selected | Improvement |
|---|---:|---:|---:|
| Features | 267 | 192 | 75 fewer |
| MAE | 17,855.86 | **17,448.28** | Improved |
| RMSE | 30,036.68 | **29,588.89** | Improved |
| R² | 0.8824 | **0.8859** | Improved |

The feature-selected model achieved better results across all three evaluation metrics while using fewer features.

## 10. Key Findings

- Feature engineering created more meaningful representations of property characteristics.
- One-hot encoding allowed categorical property information to be incorporated into the model.
- Feature selection reduced the feature space from **267 to 192 features**.
- MAE improved from **17,855.86 to 17,448.28**.
- RMSE improved from **30,036.68 to 29,588.89**.
- R² improved from **0.8824 to 0.8859**.
- The final MAE remained below the required **$18,000** target.

## 11. Recommendations

Based on the results, the feature-selected model is preferable because it provides slightly better predictive performance with fewer input features.

For further improvement, future work could explore additional feature engineering, hyperparameter tuning, and alternative regression algorithms.

## 12. Final Conclusion

The task successfully demonstrated how feature engineering and feature selection can improve a machine learning regression workflow.

The final model reduced the feature set from **267 to 192 features** and improved MAE from **17,855.86 to 17,448.28**, while also improving RMSE and R².

Most importantly, the final MAE of **17,448.28** achieved the business target of keeping prediction error below **$18,000**. The results show that carefully engineered and selected features can provide better model performance with a more compact feature set.
