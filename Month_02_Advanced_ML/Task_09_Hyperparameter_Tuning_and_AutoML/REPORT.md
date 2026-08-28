# Task 09 — Hyperparameter Tuning and AutoML

## 1. Task Overview

This task focused on improving and comparing machine learning classification models using hyperparameter optimization, class balancing, early stopping, and automated machine learning. The experiments were performed on the Wine Quality Dataset after converting the original quality score into a binary classification problem.

## 2. Objectives

The main objectives of this task were to:

* Prepare the Wine Quality Dataset for binary classification.
* Establish a baseline Logistic Regression model.
* Investigate the effect of class balancing on model performance.
* Explore model optimization and hyperparameter tuning.
* Apply early stopping to a neural network.
* Use TPOT for automated machine learning.
* Compare models using Accuracy, Precision, Recall, and F1-Score.
* Select a suitable final model based on the classification objective.

## 3. Dataset and Target Preparation

The Wine Quality Dataset initially contained **1,599 records and 12 columns**, consisting of 11 physicochemical features and the original `quality` variable.

The original quality scores were converted into a binary target named `quality_label`.

| Class | Records | Percentage |
| ----- | ------: | ---------: |
| 0     |    1175 |     86.46% |
| 1     |     184 |     13.54% |

The resulting dataset showed a noticeable class imbalance.

After data preparation, the modeling dataset contained **1,359 samples and 11 features**.

## 4. Data Preprocessing

The following preprocessing steps were completed:

1. Dataset structure and data types were inspected.
2. The original quality distribution was examined.
3. The `quality` variable was transformed into the binary `quality_label` target.
4. Features and target were separated.
5. The data was divided into training and testing sets.
6. Feature scaling was applied.
7. Class balancing was incorporated into the Logistic Regression model.

The final data split consisted of:

* **Training samples:** 1,087
* **Testing samples:** 272
* **Features:** 11

## 5. Models and Optimization

### 5.1 Logistic Regression

A standard Logistic Regression model was trained as the baseline. It provided a reference point for evaluating the effect of subsequent optimization and class balancing.

### 5.2 Balanced Logistic Regression

A balanced Logistic Regression model was then evaluated to improve the detection of the minority class.

The balanced model produced a substantial improvement in Recall compared with the baseline model.

### 5.3 Early Stopping Neural Network

A neural network was trained using early stopping. The training process stopped after **45 iterations**, preventing unnecessary additional training.

Although the model achieved high Precision, its Recall was very low, resulting in a comparatively low F1-Score.

### 5.4 TPOT AutoML

TPOT AutoML was used to automatically explore machine learning pipelines and identify an effective classification approach.

TPOT achieved the strongest overall evaluation metrics among the approaches tested.

## 6. Model Evaluation Results

The models were evaluated using Accuracy, Precision, Recall, and F1-Score.

| Model                         | Accuracy | Precision | Recall | F1-Score |
| ----------------------------- | -------: | --------: | -----: | -------: |
| Logistic Regression           |   0.8750 |    0.6000 | 0.2432 |   0.3462 |
| Balanced Logistic Regression  |   0.7904 |    0.3750 | 0.8108 |   0.5128 |
| Early Stopping Neural Network |   0.8750 |    1.0000 | 0.0698 |   0.1304 |
| TPOT AutoML                   |   0.9281 |    0.6923 | 0.8372 |   0.7579 |

## 7. Results Analysis

The baseline Logistic Regression model achieved **87.50% accuracy**, but its Recall of **0.2432** showed that it identified only a limited portion of the minority class.

After applying class balancing, Recall increased to **0.8108**, although overall Accuracy decreased to **79.04%**. This demonstrates the trade-off between overall accuracy and minority-class detection.

The Early Stopping Neural Network achieved **100% Precision**, but its Recall was only **0.0698**, indicating that it predicted very few positive cases.

TPOT AutoML achieved the highest overall results, with:

* **Accuracy:** 0.9281
* **Precision:** 0.6923
* **Recall:** 0.8372
* **F1-Score:** 0.7579

These results indicate that the automated approach provided a stronger overall balance between Precision and Recall among the tested approaches.

## 8. Final Model Selection

The final model selected in the notebook was **Balanced Logistic Regression**.

Its final evaluation results were:

* **Accuracy:** 0.7904
* **Precision:** 0.3750
* **Recall:** 0.8108
* **F1-Score:** 0.5128

The model was selected because of its significantly improved Recall for the minority class. Since the dataset was imbalanced, identifying positive cases was an important consideration during model selection.

The final Logistic Regression model and feature scaler were saved for later use.

## 9. Key Findings

* The dataset contained a significant class imbalance.
* Accuracy alone did not provide a complete picture of model performance.
* Class balancing greatly improved minority-class Recall.
* The baseline model achieved better Accuracy but weaker minority-class detection.
* The Early Stopping Neural Network produced very high Precision but poor Recall.
* TPOT AutoML achieved the strongest overall metrics among the tested approaches.
* Model selection should consider the specific classification objective and the balance between Precision and Recall.

## 10. Learning Outcomes

This task provided practical experience with:

* Hyperparameter tuning and model optimization.
* Binary classification with imbalanced data.
* Feature scaling and class balancing.
* Early stopping in neural network training.
* Automated machine learning using TPOT.
* Comparing models using multiple evaluation metrics.
* Selecting models according to the requirements of a classification problem.
* Saving and reusing trained machine learning models and preprocessing components.

## 11. Conclusion

Task 09 demonstrated the impact of optimization and model-selection strategies on classification performance. Different approaches produced different strengths across Accuracy, Precision, Recall, and F1-Score. TPOT AutoML achieved the best overall evaluation metrics, while Balanced Logistic Regression was selected as the final model because it provided substantially improved minority-class Recall. Overall, the task highlighted the importance of evaluating multiple metrics and selecting a model according to the requirements of the problem rather than relying on Accuracy alone.
