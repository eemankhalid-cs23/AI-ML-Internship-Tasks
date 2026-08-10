# Task 02 - Advanced Data Cleaning and Preprocessing

## Project Overview

This project focuses on cleaning and preprocessing the Adult Census Income dataset to prepare it for machine learning. The preprocessing pipeline improves data quality by handling missing values, removing duplicate records, detecting outliers, encoding categorical variables, scaling numerical features, and validating the final dataset.

---

## Business Problem

An HR Analytics company wants to predict employee income using historical employee information. However, the dataset contains missing values, duplicate records, inconsistent formatting, and categorical features that cannot be directly used in machine learning models.

The objective of this project is to transform the raw dataset into a clean and machine-learning-ready dataset.

---

## Dataset

**Dataset Name:** Adult Census Income Dataset (UCI / Kaggle)

**Target Variable:**
- Income (`<=50K` or `>50K`)

---

## Objectives

- Explore the dataset
- Identify missing values
- Handle missing values using appropriate techniques
- Detect and remove duplicate records
- Analyze outliers using Box Plots and IQR
- Encode categorical variables using One-Hot Encoding
- Scale numerical features using StandardScaler
- Validate the final dataset

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Google Colab
- VS Code

---

## Project Structure

```
Task_02_Advanced_Data_Cleaning_and_Preprocessing/
│
├── data/
│   └── adult.csv
│
├── notebook/
│   └── Task_02_Advanced_Data_Cleaning_and_Preprocessing.ipynb
│
├── src/
│
├── REPORT.md
├── README.md
└── requirements.txt
```

---

## Data Preprocessing Steps

- Dataset Exploration
- Missing Value Analysis
- Missing Value Imputation (Mode)
- Duplicate Detection and Removal
- Outlier Detection using Box Plots
- Outlier Analysis using IQR
- One-Hot Encoding
- Feature Scaling using StandardScaler
- Data Validation

---

## Results

After preprocessing:

- Missing Values = **0**
- Duplicate Records = **0**
- Final Dataset Shape = **(32537, 98)**

The dataset is now clean, consistent, and ready for machine learning model development.

---

## How to Run

1. Clone the repository.
2. Install the required libraries from `requirements.txt`.
3. Open the notebook in Google Colab or VS Code.
4. Run all cells in sequence.
5. Review the generated outputs and visualizations.

---

## Learning Outcomes

This project helped in understanding:

- Data cleaning techniques
- Missing value handling
- Duplicate removal
- Outlier analysis
- Feature encoding
- Feature scaling
- Data validation
- Building a preprocessing pipeline for machine learning

---

## Future Improvements

- Apply advanced outlier treatment techniques.
- Build a machine learning classification model.
- Perform feature selection.
- Evaluate multiple machine learning algorithms.

---

## Author

**Eeman Khalid**

BS Computer Science
