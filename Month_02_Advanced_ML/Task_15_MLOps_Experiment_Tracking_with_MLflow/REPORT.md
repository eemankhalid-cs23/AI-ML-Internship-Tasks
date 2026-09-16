# Task 15 — MLOps Experiment Tracking with MLflow

## 1. Objective

The objective of this task was to implement an MLOps workflow using MLflow for experiment tracking, model evaluation, artifact management, model logging, model versioning, and reproducibility.

## 2. Dataset

The Bank Marketing dataset was reused for this task. It contains 41,188 records and 20 input features. The target variable `y` indicates whether a customer subscribed to a term deposit.

The dataset was cleaned by standardizing column names, removing quotation marks from values, converting the target variable into binary format, and checking for missing values. No missing values remained after cleaning.

## 3. Data Preparation

The dataset was divided into training and testing sets using an 80/20 stratified split with `random_state=42`.

The features were divided into 10 numerical and 10 categorical variables. Numerical features were standardized using `StandardScaler`, while categorical features were transformed using `OneHotEncoder`.

A Scikit-learn preprocessing and classification pipeline was used to maintain consistent transformations and reduce the risk of data leakage.

## 4. Baseline Model

Logistic Regression was selected as the baseline model with `max_iter=2000`.

The model achieved:

| Metric    |  Score |
| --------- | -----: |
| Accuracy  | 0.9166 |
| Precision | 0.7118 |
| Recall    | 0.4364 |
| F1-Score  | 0.5411 |

The model parameters and evaluation metrics were logged as an MLflow run.

## 5. Random Forest Experiment

A Random Forest classifier was trained using 100 estimators, a maximum depth of 10, and `random_state=42`.

The results were:

| Metric    |  Score |
| --------- | -----: |
| Accuracy  | 0.9135 |
| Precision | 0.7961 |
| Recall    | 0.3114 |
| F1-Score  | 0.4477 |

The Random Forest experiment was also tracked in MLflow, allowing both models to be compared using the same evaluation metrics.

## 6. Practical MLflow Implementation

### Experiment and Run Tracking

A dedicated MLflow experiment named `Bank_Marketing_Classification` was created. Separate runs were used to track the Logistic Regression and Random Forest experiments, as well as model and artifact logging activities.

### Parameter and Metric Logging

MLflow was used to record important parameters including model type, `max_iter`, `n_estimators`, `max_depth`, `test_size`, and `random_state`.

The evaluation metrics recorded for the experiments included accuracy, precision, recall, and F1-score.

### Artifact Management

A Logistic Regression confusion matrix was generated and saved as an image artifact. The experiment comparison results were also exported to `mlflow_experiment_comparison.csv`.

A performance comparison visualization was created to compare the tracked model results.

### Experiment Comparison

The tracked MLflow runs were retrieved using `mlflow.search_runs()` and compared using their parameters and evaluation metrics.

The comparison showed that Logistic Regression achieved higher recall and F1-score, while the tested Random Forest configuration achieved higher precision.

## 7. MLflow Model Management

### Model Logging

The trained Logistic Regression pipeline was logged as an MLflow model. This stored the complete preprocessing and classification pipeline for later reuse.

### Model Loading

The stored model was loaded from its MLflow run using its model URI. The loaded model generated predictions on the test dataset without retraining.

The loaded model reproduced the original results:

| Metric    |  Score |
| --------- | -----: |
| Accuracy  | 0.9166 |
| Precision | 0.7118 |
| Recall    | 0.4364 |
| F1-Score  | 0.5411 |

### Model Registry

The Logistic Regression model was registered in the MLflow Model Registry under:

`Bank_Marketing_Logistic_Regression`

Model version 1 was successfully created and managed through the registry.

### Model Alias

The registered model version was assigned the `champion` alias. The model was then loaded using the alias:

`models:/Bank_Marketing_Logistic_Regression@champion`

The alias-based model generated predictions successfully and reproduced the same evaluation results.

This demonstrated stable model referencing and practical model lifecycle management.

## 8. Reproducibility

The main experiment configuration was documented to support reproducibility:

* Test size: 0.20
* Random state: 42
* Stratified split: True
* Categorical encoding: OneHotEncoder
* Numerical scaling: StandardScaler
* Model: Logistic Regression
* Maximum iterations: 2000

The model loaded through the `champion` alias produced the same evaluation results as the original model, confirming consistent model reuse.

## 9. Key Results

| Model               | Accuracy | Precision | Recall | F1-Score |
| ------------------- | -------: | --------: | -----: | -------: |
| Logistic Regression |   0.9166 |    0.7118 | 0.4364 |   0.5411 |
| Random Forest       |   0.9135 |    0.7961 | 0.3114 |   0.4477 |

The results demonstrate that the two models produced different performance characteristics. Logistic Regression achieved higher recall and F1-score, while Random Forest achieved higher precision under the tested configurations.

## 10. Key Insights

* MLflow successfully tracked multiple experiments and their results.
* Parameters and evaluation metrics were recorded for reproducibility.
* Evaluation visualizations were stored as artifacts.
* The trained model was logged and successfully loaded without retraining.
* Model Registry provided versioned model management.
* The `champion` alias provided a stable reference to the registered model.
* The alias-loaded model reproduced the original evaluation results.
* Experiment results were exported to CSV for further documentation and analysis.

## 11. Limitations

Only a limited number of model configurations were tested, and extensive hyperparameter tuning was not performed. The target classes are also imbalanced, so accuracy alone may not fully represent performance on the minority subscription class.

The task demonstrated model registry and lifecycle management through MLflow aliases; it did not involve an actual production deployment.

## 12. Conclusion

This task demonstrated a complete practical MLflow workflow using the Bank Marketing dataset. The workflow covered data preparation, baseline modeling, experiment tracking, parameter and metric logging, artifact management, model comparison, model logging and loading, Model Registry, alias-based model management, and reproducibility.

The successful reuse of the registered Logistic Regression model through the `champion` alias and the reproduction of its original evaluation results demonstrated how MLflow can support organized, traceable, and reproducible machine learning workflows.
