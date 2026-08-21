# Task 07 — Unsupervised Learning and Customer Segmentation

## Overview

In this task, I worked on customer segmentation using the Mall Customer Segmentation dataset. The aim was to identify different groups of customers based on their age, annual income, and spending behavior so that the results could be interpreted as useful customer personas for targeted marketing.

## What I Did

* Explored and checked the dataset for missing values and duplicates
* Analyzed customer distributions and relationships between important features
* Selected Age, Annual Income, and Spending Score for clustering
* Scaled the features before applying clustering algorithms
* Built and evaluated K-Means clustering using the Elbow Method and Silhouette Score
* Applied DBSCAN and Agglomerative Hierarchical Clustering for comparison
* Used PCA to visualize the customer clusters
* Created cluster profiles and interpreted the final groups as customer personas
* Compared the results and selected the most practical approach for the business scenario

## Results

K-Means, DBSCAN, and Hierarchical Clustering were evaluated during this task. DBSCAN achieved the highest Silhouette Score, but many customers were classified as noise. For this reason, K-Means was selected as the final approach because it produced six practical customer segments and assigned every customer to a cluster.

The final K-Means model achieved a **Silhouette Score of 0.4284**.

## Key Skills

* K-Means Clustering
* DBSCAN
* Hierarchical Clustering
* Elbow Method
* Silhouette Analysis
* Feature Scaling
* PCA Visualization
* Cluster Profiling and Interpretation
* Customer Segmentation

## Tools Used

Python, Pandas, NumPy, Matplotlib, Seaborn, and Scikit-learn.

## Project Structure

```text id="9q75nt"
Task_07_Unsupervised_Learning_and_Customer_Segmentation/
│
├── data/
│   └── .gitkeep
├── notebooks/
│   └── Task_07_Unsupervised_Learning_and_Customer_Segmentation.ipynb
├── src/
│   └── .gitkeep
├── README.md
└── REPORT.md
```

## Conclusion

This task helped me understand how unsupervised learning can be used to find meaningful customer patterns without predefined labels. By comparing different clustering algorithms, I learned that the best model should not be selected only based on one evaluation score, but also on how practical and useful the resulting segments are for the actual business problem.

