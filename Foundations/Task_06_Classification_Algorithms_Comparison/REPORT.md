# Task 06 — Classification Modeling and Business Evaluation

## 1. Introduction

This task focused on building a classification system for predicting whether a customer would subscribe to a bank term deposit. The main objective was to compare different classification models, handle class imbalance, and select a model based on both machine learning performance and business requirements.

The **Bank Marketing dataset** was used for this task.

## 2. Dataset and Initial Checks

The dataset contained customer and campaign-related information used to predict the target variable `y`.

Initial checks showed:

* **41,188 rows** and **21 columns**.
* No missing values were found.
* **12 duplicate records** were identified and removed.
* The target variable was converted into binary form: `no = 0` and `yes = 1`.

The dataset had a significant class imbalance, with approximately:

* **Non-subscribers:** 88.73%
* **Subscribers:** 11.27%

Because of this imbalance, accuracy alone was not considered sufficient for model evaluation.

## 3. Data Preparation

The data was divided into training and testing sets using a **stratified split** to preserve the target class distribution.

Numerical features were standardized using **StandardScaler**, while categorical features were transformed using **One-Hot Encoding**.

The preprocessing steps were applied consistently during model training and testing.

## 4. Classification Models

Several classification algorithms were evaluated:

* Logistic Regression
* Decision Tree
* Random Forest
* Support Vector Machine (SVM)
* K-Nearest Neighbors (KNN)

The models were evaluated using:

* Accuracy
* Precision
* Recall
* F1-score
* ROC-AUC
* PR-AUC

## 5. Handling Class Imbalance

Because the positive class represented only 11.27% of the dataset, class imbalance techniques were explored.

**Class weighting** was used to give greater importance to the minority class, while **SMOTE** was used to generate synthetic minority samples.

These approaches helped improve the models' ability to identify potential subscribers.

## 6. Threshold Tuning

The business problem assigned different costs to classification errors:

* **False Positive cost:** $5
* **False Negative cost:** $500

Since a false negative was much more expensive, identifying potential subscribers was given higher priority.

A probability threshold of **0.25** was selected instead of the default 0.50 threshold to improve positive-class detection.

## 7. Final Model Results

After comparing the models and considering the business requirements, **Balanced Random Forest** was selected as the final model.

| Metric    | Result |
| --------- | -----: |
| Accuracy  | 0.7642 |
| Precision | 0.3222 |
| Recall    | 0.9903 |
| F1-score  | 0.4862 |
| ROC-AUC   | 0.9444 |
| PR-AUC    | 0.6399 |

The model achieved a very high Recall of **0.9903**, showing that it successfully identified almost all positive subscriber cases.

## 8. Key Observations

1. The dataset contained a strong class imbalance.
2. Accuracy alone was not suitable for judging model performance.
3. Class weighting and SMOTE helped address the minority class.
4. Threshold tuning allowed the model to better match the business objective.
5. Balanced Random Forest provided strong positive-class detection.
6. False negatives were more costly than false positives, making Recall an important metric.

## 9. Learning Outcomes

Through this task, I gained practical experience with:

* Binary classification
* Data preprocessing
* Stratified train/test splitting
* Feature scaling
* One-Hot Encoding
* Multiple classification algorithms
* Class imbalance handling
* SMOTE and class weighting
* Confusion matrix analysis
* ROC-AUC and PR-AUC
* Threshold tuning
* Business cost analysis
* Model comparison and selection

## 10. Conclusion

This task demonstrated a complete classification workflow, from data preparation and model training to imbalance handling and business-oriented evaluation.

The **Balanced Random Forest** was selected as the final model, achieving **0.7642 Accuracy, 0.3222 Precision, 0.9903 Recall, 0.4862 F1-score, 0.9444 ROC-AUC, and 0.6399 PR-AUC**.

The task showed that a suitable machine learning model should be selected not only according to statistical metrics but also according to the actual business cost of prediction errors.
