# Task 10 — Pipeline Engineering with Scikit-Learn

## Overview

This task focused on building a reproducible and production-ready machine learning pipeline using Scikit-Learn. The Titanic dataset was used to combine data preprocessing, custom feature engineering, model training, evaluation, and serialization into a single consistent workflow.

## Objectives

* Build an end-to-end Scikit-Learn Pipeline.
* Apply `ColumnTransformer` for numerical and categorical preprocessing.
* Implement a custom transformer for feature engineering.
* Demonstrate `FeatureUnion` for combining feature-processing branches.
* Prevent preprocessing inconsistencies and data leakage.
* Serialize and reload the complete pipeline using Joblib.
* Compare the pipeline with a simple baseline model.

## Dataset

**Dataset:** Titanic (Kaggle)
**Target Variable:** `Survived`

The dataset contains passenger information such as passenger class, age, gender, fare, family-related attributes, and other passenger characteristics.

## Methodology

The workflow included:

1. Dataset loading and exploratory analysis
2. Data cleaning and feature selection
3. Train-test splitting
4. Custom feature engineering using `FamilySizeTransformer`
5. Numerical and categorical preprocessing with `ColumnTransformer`
6. Complete Random Forest machine learning pipeline
7. Logistic Regression baseline
8. Model evaluation and comparison
9. `FeatureUnion` demonstration
10. Pipeline serialization and reload verification

All preprocessing and feature engineering steps were kept inside the pipeline to ensure that the same transformations are applied during training and inference.

## Results

| Model                        |   Accuracy | Precision |     Recall |   F1-Score |
| ---------------------------- | ---------: | --------: | ---------: | ---------: |
| Logistic Regression Baseline |     80.45% |    79.31% |     66.67% |     72.44% |
| **Random Forest Pipeline**   | **80.45%** |    77.42% | **69.57%** | **73.28%** |

The Random Forest pipeline achieved the same accuracy as the baseline while providing better recall and F1-score.

## Pipeline Serialization

The complete trained pipeline was serialized using Joblib. Reloading the saved pipeline produced the same predictions while preserving the preprocessing and modeling workflow.

## Leakage Prevention and Reproducibility

The pipeline ensures that preprocessing is fitted using training data and consistently applied to unseen test data. Keeping transformations and modeling together reduces the risk of data leakage and prevents differences between training and inference workflows.

## Technologies

* Python
* Pandas
* NumPy
* Scikit-Learn
* Matplotlib
* Seaborn
* Joblib

## Repository Structure

```text
Task_10_Pipeline_Engineering_with_Scikit_Learn/
├── data/
├── models/
├── src/
├── Task_10_Pipeline_Engineering_with_Scikit_Learn.ipynb
├── README.md
├── REPORT.md
├── requirements.txt
└── .gitignore
```

## How to Run

1. Clone the repository.
2. Place the Titanic dataset inside the `data/` directory.
3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Open and run:

```text
Task_10_Pipeline_Engineering_with_Scikit_Learn.ipynb
```

## Key Findings

The main achievement of this task was pipeline engineering rather than only model performance. Combining feature engineering, preprocessing, and modeling into one serialized workflow makes the solution more consistent, reusable, and suitable for deployment.

## Learning Outcomes

This task strengthened practical understanding of:

* Scikit-Learn Pipelines
* ColumnTransformer
* Custom Transformers
* FeatureUnion
* Data leakage prevention
* Model serialization with Joblib
* Reproducible machine learning workflows
* Baseline model comparison

## Conclusion

Task 10 demonstrated how Scikit-Learn pipelines can transform a notebook-based machine learning workflow into a clean, modular, reproducible, and deployment-oriented solution.

