# Task 06 — Classification Algorithms Comparison

## Overview

In this task, I worked on a bank marketing classification problem. The main goal was to predict whether a customer would subscribe to a term deposit and to compare different classification algorithms for this problem.

The dataset was imbalanced, so this task was not only about finding the model with the highest accuracy. I also focused on identifying subscribers correctly and understanding the business impact of different prediction errors.

## What I Did

I started by loading and exploring the Bank Marketing dataset. I checked the dataset structure, data types, missing values, duplicate records and target distribution. There were no missing values, while 12 duplicate rows were removed during data cleaning.

After cleaning the data, I encoded the target variable and prepared the features for modelling. I used a stratified train-test split so that the class distribution remained similar in both datasets. Numerical features were scaled and categorical features were encoded using a preprocessing pipeline to avoid data leakage.

I first created a simple baseline model and then trained and compared five classification algorithms:

- Logistic Regression
- Decision Tree
- Random Forest
- Support Vector Machine (SVM)
- K-Nearest Neighbors (KNN)

The models were evaluated using Accuracy, Precision, Recall, F1-Score, ROC-AUC and PR-AUC. The baseline achieved high accuracy because most customers belonged to the non-subscriber class, but it could not identify actual subscribers. This showed why accuracy alone was not enough for this dataset.

## Handling Class Imbalance

The positive class represented a much smaller portion of the dataset, so I tested different approaches to improve minority-class detection.

I applied class weights to suitable models and also used SMOTE on the training data. I compared these approaches with the standard models to see how they affected recall, precision and overall model performance.

## Final Model and Business Decision

The final approach was **Balanced Random Forest**. Instead of keeping the default prediction threshold of 0.50, I tested different thresholds based on the business problem.

In this scenario, a false positive costs only **$5**, while missing a potential subscriber has an estimated cost of **$500**. Because false negatives were much more expensive, I selected **0.25** as the final threshold.

With this threshold, the model achieved:

- **Accuracy:** 76.42%
- **Recall:** 99.03%
- **ROC-AUC:** 94.44%
- **PR-AUC:** 63.99%
- **Estimated Cost Reduction:** 96.95%

The final result showed that choosing a model should depend on the actual problem and business objective, not only on accuracy.

## What I Learned

Through this task, I learned how to compare multiple classification algorithms and understand that different models can perform differently depending on the dataset and evaluation metric.

I also learned how to:

- Compare Logistic Regression, Decision Tree, Random Forest, SVM and KNN
- Build and evaluate a baseline model
- Handle class imbalance using class weights and SMOTE
- Use Precision, Recall, F1-Score, ROC-AUC and PR-AUC for model evaluation
- Understand why high accuracy can be misleading on imbalanced data
- Use ROC and Precision-Recall curves for classification analysis
- Tune the prediction threshold according to business requirements
- Connect machine learning results with business cost and decision-making

## Tools Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Imbalanced-learn
- Matplotlib
- Seaborn
- Google Colab

## Project Structure

```text
Task_06_Classification_Algorithms_Comparison/
│
├── Task_06_Classification_Algorithms_Comparison.ipynb
├── README.md
├── REPORT.md
├── requirements.txt
│
├── src/
│   └── classification_helpers.py
│
└── figures/

## Conclusion

This task helped me understand the complete process of solving an imbalanced classification problem. I compared multiple models, handled class imbalance using different techniques and selected the final approach based on both model performance and business cost.

The most important learning from this project was that **the model with the highest accuracy is not always the best model**. In this case, reducing costly false negatives was more important, so threshold optimization played an important role in the final decision.
