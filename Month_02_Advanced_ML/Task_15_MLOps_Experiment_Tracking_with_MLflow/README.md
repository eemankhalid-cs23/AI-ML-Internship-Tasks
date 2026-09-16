# Task 15 — MLOps Experiment Tracking with MLflow

## Overview

This task demonstrates experiment tracking and model management using MLflow on the Bank Marketing dataset.

## Key Skills

* MLflow experiment and run tracking
* Parameter and metric logging
* Artifact management
* Model logging and loading
* Model Registry and aliases
* Experiment comparison
* Reproducibility

## Dataset

Bank Marketing dataset containing 41,188 records and 20 input features. The target variable `y` indicates whether a customer subscribed to the term deposit.

## Models

* Logistic Regression
* Random Forest

## Results

| Model               | Accuracy | Precision | Recall | F1-Score |
| ------------------- | -------: | --------: | -----: | -------: |
| Logistic Regression |   0.9166 |    0.7118 | 0.4364 |   0.5411 |
| Random Forest       |   0.9135 |    0.7961 | 0.3114 |   0.4477 |

The Logistic Regression model was registered in MLflow and assigned the `champion` alias. The alias-loaded model reproduced the same evaluation results, supporting reproducible model reuse.

## Project Structure

```text
data/        Dataset placeholder
figures/     Evaluation visualizations
src/         Source code
notebook     Complete MLflow workflow
REPORT.md    Task report
```

## Tools

Python, Scikit-learn, Pandas, NumPy, Matplotlib, and MLflow.

