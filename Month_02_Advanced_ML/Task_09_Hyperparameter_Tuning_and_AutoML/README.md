# Task 09 — Hyperparameter Tuning and AutoML

## Overview

This task focuses on improving machine learning model performance through hyperparameter tuning, model optimization, early stopping, and automated machine learning techniques.

## Objective

The main objectives were to:

* Prepare the dataset for binary classification.
* Establish and evaluate a baseline model.
* Handle class imbalance and compare its effect on performance.
* Explore early stopping for neural network training.
* Apply automated machine learning using TPOT.
* Compare models using multiple evaluation metrics.

## Dataset

The **Wine Quality Dataset** was used for this task.

The dataset initially contained **1,599 records and 12 columns**, including 11 input features and the original `quality` variable.

### Target Variable

The original `quality` variable was transformed into a binary target named `quality_label`.

| Class | Records | Percentage |
| ----- | ------: | ---------: |
| 0     |    1175 |     86.46% |
| 1     |     184 |     13.54% |

After data preparation, **1,359 samples with 11 features** were used for modeling.

## Data Preparation

The following steps were performed:

* Inspected the dataset structure and data types.
* Examined the original quality distribution.
* Created the binary `quality_label` target.
* Separated features and target.
* Split the data into training and testing sets.
* Applied feature scaling.
* Used class balancing for Logistic Regression.

The final split contained:

* Training data: **1,087 samples**
* Testing data: **272 samples**
* Features: **11**

## Models and Techniques

The following approaches were explored:

* Logistic Regression
* Balanced Logistic Regression
* Early Stopping Neural Network
* TPOT AutoML
* Hyperparameter optimization

## Model Evaluation

The models were evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix
* Classification Report

Since the dataset was imbalanced, Precision, Recall, and F1-Score were considered alongside Accuracy.

### Results

| Model                         | Accuracy | Precision | Recall | F1-Score |
| ----------------------------- | -------: | --------: | -----: | -------: |
| Logistic Regression           |   0.8750 |    0.6000 | 0.2432 |   0.3462 |
| Balanced Logistic Regression  |   0.7904 |    0.3750 | 0.8108 |   0.5128 |
| Early Stopping Neural Network |   0.8750 |    1.0000 | 0.0698 |   0.1304 |
| TPOT AutoML                   |   0.9281 |    0.6923 | 0.8372 |   0.7579 |

The Early Stopping Neural Network stopped after **45 training iterations**.

TPOT AutoML achieved the highest overall performance among the approaches tested, with an accuracy of **0.9281** and F1-Score of **0.7579**.

## Final Model Selection

The final model selected in the notebook was **Balanced Logistic Regression**.

Its final performance was:

* Accuracy: **0.7904**
* Precision: **0.3750**
* Recall: **0.8108**
* F1-Score: **0.5128**

The balanced model provided substantially higher recall for the minority class than the baseline Logistic Regression model. It was therefore selected as the final model based on the classification objective.

The final model and feature scaler were saved for later use.

## Key Findings

* The dataset contained a significant class imbalance.
* Class balancing improved minority-class recall considerably.
* The baseline Logistic Regression achieved higher accuracy but lower recall.
* The Early Stopping Neural Network achieved perfect precision but very low recall.
* TPOT AutoML produced the strongest overall evaluation metrics.
* Model selection depends on the evaluation objective, not accuracy alone.

## Technologies

* Python
* Pandas
* NumPy
* Scikit-learn
* TensorFlow
* TPOT
* Matplotlib
* Seaborn
* Joblib
* Jupyter Notebook / Google Colab

## Repository Structure

```text
Task_09_Hyperparameter_Tuning_and_AutoML/
│
├── data/
│   ├── .gitkeep
│   └── winequality-red.csv
│
├── Task_09_Hyperparameter_Tuning_AutoML.ipynb
├── README.md
├── REPORT.md
├── requirements.txt
└── .gitignore
```

## How to Run

1. Clone or download the repository.
2. Open `Task_09_Hyperparameter_Tuning_AutoML.ipynb` in Jupyter Notebook or Google Colab.
3. Make sure the dataset is available in the `data/` directory.
4. Install the required dependencies from `requirements.txt`.
5. Run the notebook cells sequentially.

## Learning Outcomes

This task provided practical experience with:

* Hyperparameter optimization and model tuning.
* Handling imbalanced classification data.
* Early stopping in neural network training.
* Automated machine learning using TPOT.
* Comparing classification models using multiple metrics.
* Selecting a model based on the requirements of the classification problem.

## Conclusion

Task 09 demonstrated how model optimization, class balancing, early stopping, and AutoML can affect classification performance. The experiments showed that different approaches perform differently across evaluation metrics. TPOT achieved the strongest overall metrics, while Balanced Logistic Regression was selected as the final model because of its improved minority-class recall.
