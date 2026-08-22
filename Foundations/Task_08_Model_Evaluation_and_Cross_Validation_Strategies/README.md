# Task 08 — Model Evaluation and Cross Validation Strategies

## Overview

This task focuses on evaluating machine learning models using different cross-validation strategies. The project uses a Heart Disease dataset and explores why relying on a single train-test split or accuracy score may give misleading results.

The main goal was to understand model performance more reliably by checking stability, generalization, and performance across different validation approaches.

## What I Did

- Loaded and explored the Heart Disease dataset
- Checked missing values, duplicates, data types, and class distribution
- Preprocessed numerical and categorical features using machine learning pipelines
- Built Logistic Regression and Random Forest models
- Evaluated models using Accuracy, Precision, Recall, F1-Score, and ROC-AUC
- Applied K-Fold and Stratified K-Fold Cross Validation
- Implemented Leave-One-Out Cross Validation on a smaller sample
- Used Nested Cross Validation for a more reliable performance estimate
- Created Learning Curves and Validation Curves to study model behavior
- Analyzed the bias-variance tradeoff and model limitations

## Key Findings

The results showed that accuracy alone can be misleading, especially when the target classes are imbalanced. Although the models achieved around 80% accuracy, ROC-AUC results showed that they were not reliably distinguishing between heart disease and non-heart disease cases.

Different cross-validation strategies provided a more complete view of model stability and helped avoid overly optimistic performance estimates.

## Key Learning

This task helped me understand the importance of evaluating a model with appropriate validation strategies and multiple metrics instead of relying on one score.

I also learned how K-Fold, Stratified K-Fold, Leave-One-Out, and Nested Cross Validation can be used for different evaluation purposes, while learning and validation curves help identify possible bias or variance problems.

## Conclusion

The current models achieved reasonable accuracy but were not reliable enough for clinical deployment based on the overall evaluation results. The main takeaway from this task is that a model can appear accurate while still performing poorly on the actual problem it needs to solve.

## Project Structure

```text
Task_08_Model_Evaluation_and_Cross_Validation_Strategies/
│
├── data/
│   └── dataset.csv
│
├── notebooks/
│   └── Task_08.ipynb
│
├── src/
├── README.md
├── REPORT.md
└── requirements.txt
