# Task 10 — Pipeline Engineering with Scikit-Learn

## 1. Introduction

This task focused on developing a complete machine learning pipeline using **Scikit-Learn** for Titanic survival prediction. The objective was to combine feature engineering, preprocessing, model training, evaluation, and model saving into one reusable workflow.

Using a pipeline helps maintain consistency between training and prediction while reducing the risk of preprocessing errors and data leakage.

---

## 2. Objectives

The main objectives of this task were to:

* Build an end-to-end Scikit-Learn pipeline.
* Apply feature engineering within the pipeline.
* Handle numerical and categorical features separately.
* Use `ColumnTransformer` for preprocessing.
* Train a machine learning classification model.
* Evaluate the complete pipeline on unseen data.
* Save and reload the trained pipeline.
* Understand the importance of reproducible and production-ready ML workflows.

---

## 3. Dataset

The **Titanic dataset** was used for this task.

The target variable was:

* `Survived` — `0` represents did not survive and `1` represents survived.

The main features included:

* `Pclass`
* `Age`
* `Sex`
* `SibSp`
* `Parch`
* `Fare`
* `Embarked`

A new `FamilySize` feature was also created during feature engineering.

---

## 4. Data Preprocessing

The preprocessing steps were incorporated directly into the pipeline.

### Numerical Features

Numerical features were processed using:

* Median imputation for missing values.
* `StandardScaler` for feature scaling.

### Categorical Features

Categorical features were processed using:

* Most-frequent-value imputation.
* `OneHotEncoder`.

The encoder used `handle_unknown="ignore"` so that unseen categories would not cause errors during prediction.

---

## 5. Feature Engineering

A custom transformer was created to generate the `FamilySize` feature.

The feature was calculated as:

```text
FamilySize = SibSp + Parch + 1
```

The custom transformer was implemented using Scikit-Learn's `BaseEstimator` and `TransformerMixin`.

Integrating this transformation into the pipeline ensures that the same feature engineering step is automatically applied to new data.

---

## 6. ColumnTransformer

`ColumnTransformer` was used to apply appropriate preprocessing to different feature groups.

The preprocessing structure was:

```text
Numerical Features
    → Median Imputation
    → StandardScaler

Categorical Features
    → Most-Frequent Imputation
    → OneHotEncoder
```

This allowed all preprocessing operations to be handled together within the overall pipeline.

---

## 7. Machine Learning Pipeline

The complete workflow was organized as:

```text
Raw Data
   ↓
Feature Engineering
   ↓
ColumnTransformer
   ↓
Preprocessing
   ↓
Random Forest Classifier
   ↓
Predictions
   ↓
Evaluation
```

The use of a single pipeline ensures that feature engineering and preprocessing are performed consistently during both training and inference.

---

## 8. Model Training

A **Random Forest Classifier** was used as the main model.

The model was configured with:

* `n_estimators = 200`
* `class_weight = "balanced"`
* `random_state = 42`

The classifier was placed at the end of the pipeline so that it automatically receives the processed features.

---

## 9. Model Performance

The final Random Forest pipeline achieved the following results on the test set:

| Metric    |  Score |
| --------- | -----: |
| Accuracy  | 0.8045 |
| Precision | 0.7742 |
| Recall    | 0.6957 |
| F1-Score  | 0.7328 |

The pipeline achieved an overall test accuracy of **80.45%**.

---

## 10. Baseline Comparison

A Logistic Regression model was used as a baseline for comparison.

| Model                  | Accuracy | Precision | Recall | F1-Score |
| ---------------------- | -------: | --------: | -----: | -------: |
| Logistic Regression    |   0.8045 |    0.7931 | 0.6667 |   0.7244 |
| Random Forest Pipeline |   0.8045 |    0.7742 | 0.6957 |   0.7328 |

Both models achieved the same accuracy. However, the Random Forest pipeline produced better recall and F1-score, while Logistic Regression achieved slightly higher precision.

This shows that the main benefit of the pipeline was not a large accuracy improvement, but rather a **more consistent and reusable ML workflow**.

---

## 11. Model Serialization

The complete trained pipeline was saved using **Joblib**.

Saving the complete pipeline preserves:

* Feature engineering
* Missing-value handling
* Feature scaling
* Categorical encoding
* Trained Random Forest model

The saved pipeline can therefore be loaded later and directly used for predictions without manually repeating the preprocessing steps.

---

## 12. Pipeline Verification

After saving, the pipeline was loaded again to verify its functionality.

The reloaded pipeline achieved:

* **Accuracy:** 0.8045
* **Predictions identical to the original pipeline:** `True`

This confirmed that the complete workflow was successfully preserved during serialization.

---

## 13. Key Findings

The main findings from the task were:

* A complete ML workflow can be organized using Scikit-Learn pipelines.
* Custom feature engineering can be integrated into the pipeline.
* `ColumnTransformer` allows different preprocessing techniques for different feature types.
* Pipelines help maintain consistent preprocessing between training and prediction.
* The Random Forest pipeline achieved **80.45% accuracy**.
* Random Forest provided slightly better recall and F1-score than the Logistic Regression baseline.
* The complete pipeline was successfully saved and reloaded.
* Identical predictions after reloading confirmed successful serialization.

---

## 14. Challenges

Some of the main challenges involved:

* Selecting appropriate preprocessing methods for different feature types.
* Integrating custom feature engineering into the pipeline.
* Handling missing values correctly.
* Maintaining consistent transformations between training and test data.
* Ensuring that the saved pipeline could be successfully reloaded.

These challenges improved understanding of practical machine learning pipeline development.

---

## 15. Learning Outcomes

This task strengthened my understanding of:

* Scikit-Learn `Pipeline`
* `ColumnTransformer`
* Custom transformers
* Feature engineering
* Missing-value handling
* Feature scaling
* One-hot encoding
* Random Forest classification
* Model evaluation
* Data leakage prevention
* Model serialization
* Reusable and reproducible ML workflows

---

## 16. Conclusion

Task 10 demonstrated how Scikit-Learn can be used to create a structured and reusable machine learning pipeline.

The final pipeline combined feature engineering, preprocessing, and Random Forest classification into a single workflow and achieved **80.45% test accuracy**.

Although its accuracy was the same as the Logistic Regression baseline, the pipeline provided a more reliable and maintainable approach by keeping preprocessing and prediction together.

Successfully saving and reloading the pipeline also demonstrated how the developed workflow can be reused for future predictions and practical ML applications.
