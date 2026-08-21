# Task 05 — Regression Modeling From Scratch to Production

## 1. Introduction

This task focused on building a regression-based house price prediction model and understanding how different regression techniques perform on unseen data. The main objective was to move from a simple baseline to more advanced models, compare their performance, and check whether the predictions were useful from a business perspective.

The **California Housing dataset** from Scikit-learn was used for this task.

## 2. Dataset and Initial Checks

The California Housing dataset contains numerical housing and geographical features used to predict median house values.

Before modeling, the dataset was inspected for basic data quality issues. The checks showed:

* No missing values were found.
* No duplicate records were found.
* The data was suitable for regression modeling.
* The target and input features were separated before training.

The data was then divided into training and testing sets so that the models could be evaluated on data they had not seen during training.

## 3. Data Preparation

Feature scaling was applied where required to keep the feature ranges consistent, especially for regularized and polynomial models.

For Polynomial Regression, a **degree-2 polynomial transformation** was used. The polynomial transformation and scaling were handled through a pipeline so that the same preprocessing steps were applied consistently during prediction.

## 4. Baseline Analysis

A baseline prediction was created before training the regression models. This provided a reference point for measuring how much improvement the machine learning models achieved.

The baseline results were:

* **MAE:** 0.906069
* **RMSE:** 1.144856
* **R²:** -0.000219

The almost zero and slightly negative R² showed that the baseline had very limited predictive ability.

## 5. Regression Models

### Linear Regression

Linear Regression was used as the first actual machine learning model. It produced a clear improvement over the baseline.

* **MAE:** 0.533200
* **RMSE:** 0.745581
* **R²:** 0.575788

### Ridge Regression

Ridge Regression was then tested to introduce L2 regularization and control the effect of large model coefficients.

* **MAE:** 0.533193
* **RMSE:** 0.745557
* **R²:** 0.575816

The improvement over Linear Regression was very small, but the model performed slightly better across the evaluation metrics.

### Tuned Ridge Regression

The Ridge model was further tuned to find a better configuration.

* **MAE:** 0.533138
* **RMSE:** 0.745342
* **R²:** 0.576060

The tuning produced another small improvement, showing that changing the regularization setting had a limited but measurable effect on this dataset.

### Polynomial Regression

Polynomial Regression was introduced to capture non-linear relationships that a basic linear model may not represent effectively.

A degree-2 polynomial transformation was used before fitting the regression model.

The results were:

* **MAE:** 0.467001
* **RMSE:** 0.681397
* **R²:** 0.645682

Polynomial Regression achieved the best results among all the tested models.

## 6. Model Comparison

| Model                     |          MAE |         RMSE |           R² |
| ------------------------- | -----------: | -----------: | -----------: |
| Baseline                  |     0.906069 |     1.144856 |    -0.000219 |
| Linear Regression         |     0.533200 |     0.745581 |     0.575788 |
| Ridge Regression          |     0.533193 |     0.745557 |     0.575816 |
| Tuned Ridge Regression    |     0.533138 |     0.745342 |     0.576060 |
| **Polynomial Regression** | **0.467001** | **0.681397** | **0.645682** |

The comparison shows a clear improvement from the baseline to the trained models. Ridge and tuned Ridge provided only small improvements over Linear Regression, while Polynomial Regression produced the largest improvement.

## 7. Improvement Analysis

The best modeling result showed substantial improvement compared with the baseline:

* **MAE improvement:** 48.46%
* **RMSE improvement:** 40.48%
* **R² improvement:** 0.6459

The R² increased from approximately zero for the baseline to **0.645682** for Polynomial Regression. This indicates that the final model captured considerably more of the variation in the target values.

## 8. Business Threshold Analysis

The business scenario defined an acceptable prediction error of approximately **±$30,000**. Since the target values were represented in scaled form, a threshold of **0.3** was used for the analysis.

The results were:

* **Total predictions:** 4,128
* **Acceptable predictions:** 1,849
* **Unacceptable predictions:** 2,279
* **Acceptable prediction percentage:** 44.79%

This was an important observation because the model's overall evaluation metrics improved significantly, but less than half of the predictions were within the defined business threshold.

Therefore, a model can have good average performance while still producing a considerable number of individual predictions with larger errors.

## 9. Key Observations

Several important points were observed during the modeling process:

1. The baseline was much weaker than the trained regression models.
2. Linear Regression provided a major improvement over the baseline.
3. Ridge Regression gave only a slight improvement over Linear Regression.
4. Tuning Ridge produced another small improvement.
5. Polynomial Regression performed noticeably better than the other tested models.
6. The lower MAE and RMSE of Polynomial Regression indicate more accurate predictions overall.
7. The business threshold analysis showed that overall model metrics alone are not enough to judge whether a model meets a practical business requirement.

## 10. Learning Outcomes

Through this task, I gained practical experience with:

* Regression model development
* Baseline modeling
* Train/test evaluation
* Feature scaling
* Ridge regularization
* Hyperparameter tuning
* Polynomial feature transformation
* MAE, RMSE, and R²
* Model comparison
* Prediction analysis
* Business-oriented threshold evaluation

I also learned that model selection should consider both statistical performance and the actual requirements of the business problem.

## 11. Conclusion

This task provided a complete practical workflow for regression modeling, starting with a baseline and progressing through Linear, Ridge, Tuned Ridge, and Polynomial Regression.

Polynomial Regression was the best-performing model, achieving an **MAE of 0.467001, RMSE of 0.681397, and R² of 0.645682**. Although the model significantly improved the overall prediction performance, the business threshold analysis showed that only **44.79%** of test predictions were within the acceptable error range.

Overall, the task demonstrated how different regression techniques can be compared systematically and why both model metrics and business requirements should be considered before selecting a model for practical use.
