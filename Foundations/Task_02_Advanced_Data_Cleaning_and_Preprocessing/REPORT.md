# Task 02 – Advanced Data Cleaning and Preprocessing

---

# 1. Objective

The objective of this task was to perform advanced data cleaning and preprocessing on the Adult Census Income dataset. The aim was to improve data quality by handling missing values, removing duplicate records, detecting outliers, encoding categorical variables, scaling numerical features, and validating the final dataset.

A clean and well-preprocessed dataset is essential because machine learning models require complete, consistent, and properly formatted data to produce reliable predictions.

---

# 2. Business Scenario

An HR Analytics company uses employee information to predict annual income. However, the available dataset contains several data quality issues, including missing values, duplicate records, inconsistent formatting, and categorical features that cannot be directly processed by machine learning algorithms.

If these issues are not addressed, they can lead to inaccurate salary predictions, poor model performance, and unfair decision-making. Therefore, proper preprocessing is necessary before building any machine learning model.

---

# 3. Dataset Information

**Dataset Name:** Adult Census Income Dataset (UCI/Kaggle)

**Objective:** Predict whether an individual's annual income is greater than \$50K based on demographic and employment-related attributes.

### Important Features

- Age
- Workclass
- Education
- Occupation
- Marital Status
- Relationship
- Race
- Sex
- Capital Gain
- Capital Loss
- Hours per Week
- Native Country

**Target Variable:** Income (`<=50K` or `>50K`)

---

# 4. Data Exploration

Before preprocessing, the dataset was explored to understand its structure and identify data quality issues.

The following exploratory steps were performed:

- Loaded the dataset using Pandas.
- Displayed the first few records.
- Examined the dataset dimensions.
- Reviewed data types and column information.
- Generated descriptive statistics.
- Checked missing values.
- Identified duplicate records.
- Visualized numerical features using box plots.

This exploration helped determine the appropriate preprocessing techniques for the dataset.

---

# 5. Missing Value Analysis

## Purpose

Missing values reduce data quality and may negatively affect machine learning models. Therefore, they were identified and handled before further preprocessing.

## Observation

Missing values were found only in the following categorical columns:

| Column | Missing Values |
|---------|---------------:|
| Workclass | 1836 |
| Occupation | 1843 |
| Native Country | 583 |

All other columns contained no missing values.

## Treatment

Since these columns contain categorical values, missing data was replaced using **Mode (Most Frequent Value)**. Mode imputation preserves the most common category while avoiding unnecessary data loss.

## Result

- All missing values were successfully removed.
- The dataset became complete and ready for further preprocessing.

---

# 6. Duplicate Record Analysis

## Purpose

Duplicate records can introduce bias by repeating the same information multiple times. Removing duplicates improves data quality and ensures more reliable model training.

## Observation

A duplicate check identified:

**24 duplicate records**

## Treatment

Duplicate records were removed using the `drop_duplicates()` function.

## Result

- Duplicate Records = **0**
- The dataset now contains only unique observations.

---

# 7. Outlier Detection

## Purpose

Outliers are unusually high or low values that may influence statistical analysis and machine learning models.

## Method

Outliers were explored using:

- Box Plots
- Interquartile Range (IQR) Method

The Age feature was used to demonstrate the IQR technique, while other numerical variables such as Capital Gain and Capital Loss were also visualized.

## Observation

Several numerical features contained potential outliers. These were successfully identified through visualization and IQR calculations.

## Result

The analysis provided a clear understanding of extreme values within the dataset, supporting future preprocessing and model development.

---

# 8. Categorical Feature Encoding

## Purpose

Machine learning algorithms cannot directly process categorical (text) data. Therefore, categorical variables were converted into numerical values.

## Method

One-Hot Encoding was applied using Pandas `get_dummies()` with `drop_first=True`.

One-Hot Encoding was selected because most categorical variables in this dataset are nominal and have no natural order.

Label Encoding was not used because assigning numerical labels to nominal categories may introduce incorrect ordinal relationships.

## Result

All categorical variables were successfully converted into numerical binary features suitable for machine learning.

---

# 9. Feature Scaling

## Purpose

Numerical features often have different ranges. Large differences between feature values may negatively affect machine learning algorithms.

## Method

StandardScaler from Scikit-learn was applied to standardize numerical features.

The `fit_transform()` method was used to learn the statistical properties of the data and transform numerical values into a common scale.

## Result

All numerical features were standardized, ensuring that each feature contributes fairly during model training.

---

# 10. Data Validation

After completing preprocessing, the dataset was validated to ensure data quality.

The following checks were performed:

- Missing Values = **0**
- Duplicate Records = **0**
- Final Dataset Shape = **(32537, 98)**

These results confirm that the dataset is clean, consistent, and ready for machine learning.

---

# 11. Key Learnings

During this task, the following concepts were learned and applied:

- Data exploration and profiling
- Missing value analysis and Mode imputation
- Duplicate record detection and removal
- Outlier detection using Box Plots and IQR
- One-Hot Encoding for categorical variables
- Feature Scaling using StandardScaler
- Data validation techniques
- Building a clean and reproducible preprocessing pipeline

---

# 12. Business Impact

Data preprocessing significantly improves the quality of the dataset before model development.

A clean dataset helps:

- Improve prediction accuracy
- Reduce data inconsistencies
- Prevent bias caused by duplicate or missing data
- Enhance the reliability of machine learning models
- Support fair and data-driven business decisions

---

# 13. Conclusion

This task successfully transformed the Adult Census Income dataset into a clean and machine-learning-ready dataset.

Missing values were handled, duplicate records were removed, outliers were analyzed, categorical variables were encoded, numerical features were standardized, and the final dataset was validated successfully.

The preprocessing pipeline developed in this task provides a reliable foundation for future machine learning model training and income prediction.
