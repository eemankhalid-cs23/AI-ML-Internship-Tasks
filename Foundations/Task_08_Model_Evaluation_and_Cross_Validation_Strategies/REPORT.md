# Task 08 — Model Evaluation and Cross Validation Strategies

## 1. Introduction

This task focused on evaluating machine learning models for a heart disease prediction problem using reliable validation strategies. The main purpose was to understand how model performance can change depending on the evaluation method used and why relying on a single train-test split or accuracy score can produce misleading conclusions.

The business scenario involved a hospital planning to use a heart disease prediction model. Since a previous evaluation approach had overestimated model accuracy, this task emphasized careful validation, prevention of data leakage, and a more realistic assessment of model performance before considering deployment.

---

## 2. Dataset and Initial Exploration

The Heart Disease dataset was used for this task. It contained **10,000 records and 21 columns**, with `Heart Disease Status` used as the target variable.

The dataset included a combination of numerical and categorical patient-related features such as age, gender, blood pressure, cholesterol, BMI, smoking, diabetes, exercise habits, stress level, sleep hours, triglycerides, fasting blood sugar, and CRP level.

During the initial exploration, the dataset was checked for its structure, data types, missing values, duplicate records, and target class distribution. Missing values were present in several features, while no duplicate records were found.

The target distribution also showed that the classes were imbalanced, with approximately **80% non-heart-disease cases and 20% heart-disease cases**. This made it important to use evaluation metrics beyond accuracy.

---

## 3. Data Preprocessing

The dataset was prepared using separate preprocessing steps for numerical and categorical features.

For numerical features, missing values were handled using median imputation and the values were standardized. For categorical features, missing values were replaced using the most frequent category and the features were encoded using one-hot encoding.

These preprocessing steps were placed inside machine learning pipelines. This ensured that transformations were applied correctly during model training and cross-validation and helped reduce the risk of data leakage.

The processed data was then divided into training and test sets for model development and final evaluation.

---

## 4. Baseline Model Evaluation

Logistic Regression was used as the initial model.

Instead of evaluating it only with accuracy, multiple metrics were used, including:

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC

A confusion matrix and classification report were also generated to examine model performance in more detail.

The results showed that the model achieved approximately **80% accuracy**, but this result alone was misleading because the model was not effectively distinguishing the heart disease cases. The test ROC-AUC was approximately **0.486**, showing that the model's ability to separate the two classes was weak.

This demonstrated why accuracy should not be the only metric used for an imbalanced healthcare classification problem.

---

## 5. K-Fold and Stratified K-Fold Cross Validation

K-Fold Cross Validation was applied to evaluate the model across multiple splits of the training data. This provided a broader estimate of model performance instead of depending on one validation split.

Stratified K-Fold Cross Validation was also used because of the imbalanced target classes. This approach maintained the class distribution more consistently across the folds.

Multiple metrics, including accuracy, precision, recall, F1-score, and ROC-AUC, were examined. The cross-validation results provided a clearer view of model stability and showed that high accuracy did not necessarily mean strong predictive performance.

---

## 6. Random Forest Model Comparison

A Random Forest classifier was then implemented and compared with Logistic Regression.

The same preprocessing pipeline approach was used to keep the evaluation consistent and avoid leakage. Random Forest was evaluated using the same classification metrics and Stratified K-Fold Cross Validation.

The model also achieved approximately **80% accuracy**, but its test ROC-AUC was approximately **0.485**, while the cross-validation ROC-AUC was close to **0.511**.

The comparison between Logistic Regression and Random Forest showed that changing the model did not significantly improve the ability to distinguish between heart disease and non-heart-disease cases.

---

## 7. Leave-One-Out Cross Validation

Leave-One-Out Cross Validation was also implemented to explore another evaluation strategy.

Because LOOCV can be computationally expensive for larger datasets, it was demonstrated using a smaller stratified sample. The model was repeatedly trained while one observation at a time was used for validation.

The demonstration produced a mean accuracy of approximately **0.53**, highlighting how evaluation results can vary depending on the validation strategy and sample used.

---

## 8. Nested Cross Validation

Nested Cross Validation was implemented to obtain a more reliable estimate of model performance while separating hyperparameter tuning from final evaluation.

An inner cross-validation loop was used with GridSearchCV for model tuning, while an outer cross-validation loop was used to estimate the final performance. A Random Forest pipeline was evaluated using ROC-AUC scoring.

The nested cross-validation result produced a mean ROC-AUC of approximately **0.514**. This result was still close to random performance, confirming that the model required further improvement.

---

## 9. Learning and Validation Curve Analysis

A learning curve was created for Logistic Regression using ROC-AUC as the evaluation metric.

The curve was used to compare training and validation performance as more training data was added. The analysis indicated signs of **high bias**, suggesting that the current model and features were not capturing enough useful predictive information.

A validation curve was also created to examine how changes in model settings affected training and validation performance. This helped study the relationship between model complexity and generalization through the bias-variance tradeoff.

The curve analysis showed that simply changing model settings was unlikely to solve the main performance problem.

---

## 10. Key Findings

The main findings from the task were:

- The dataset contained 10,000 records and 21 columns.
- The target classes were imbalanced, making accuracy alone insufficient for evaluation.
- Logistic Regression achieved around 80% accuracy but a test ROC-AUC of approximately 0.486.
- Random Forest also achieved around 80% accuracy but a test ROC-AUC of approximately 0.485.
- Cross-validation ROC-AUC values for both models remained close to random performance.
- LOOCV demonstrated the computational cost and different evaluation behavior of leave-one-out validation.
- Nested Cross Validation produced a mean ROC-AUC of approximately 0.514.
- Learning curve analysis indicated signs of high bias.
- Different validation strategies provided a more reliable understanding of model performance than a single evaluation score.

---

## 11. Conclusion

This task demonstrated that proper model evaluation is essential, especially for a healthcare-related prediction problem.

Although both Logistic Regression and Random Forest achieved approximately 80% accuracy, the additional evaluation metrics and cross-validation results showed that this accuracy was not enough to consider the models reliable. Their ROC-AUC values remained close to random performance, indicating weak ability to distinguish between the two target classes.

Through this task, I learned how K-Fold, Stratified K-Fold, Leave-One-Out, and Nested Cross Validation can be used for different evaluation purposes. I also gained practical experience with learning curves, validation curves, multiple classification metrics, machine learning pipelines, and data leakage prevention.

The final conclusion is that the current models should not be considered ready for clinical deployment. Further work would be needed to improve the predictive signal, features, and overall model performance before using the system in a real healthcare environment.
