# Task 07 — Unsupervised Learning and Customer Segmentation Report

## Introduction

This task focused on applying unsupervised learning to divide customers into meaningful groups based on their characteristics and spending patterns. Using the Mall Customer Segmentation dataset, the main objective was to explore different clustering techniques and identify customer segments that could support more targeted marketing decisions.

## Dataset and Preparation

The dataset contains 200 customer records with information including gender, age, annual income, and spending score. The data was checked before modeling, and no missing values or duplicate records were found.

Age, Annual Income, and Spending Score were selected as the main features for clustering. These features were standardized before applying the clustering algorithms because distance-based methods are sensitive to differences in feature scales.

## Methodology

The analysis started with exploratory data analysis to understand customer distributions and the relationships between income, age, and spending behavior.

Three clustering approaches were then implemented:

* **K-Means Clustering:** Used as the main clustering approach. The Elbow Method and Silhouette Analysis were used to evaluate different numbers of clusters.
* **DBSCAN:** Applied as a density-based clustering method, followed by parameter tuning.
* **Agglomerative Hierarchical Clustering:** Used as an additional approach for comparison.

PCA was also applied to reduce the selected features to two dimensions and visualize the resulting customer groups.

## Results and Model Selection

A K-Means baseline with 5 clusters achieved a Silhouette Score of **0.4166**. After evaluating different values of K, the final K-Means model was created with **6 clusters** and achieved a Silhouette Score of **0.4284**.

DBSCAN achieved a higher Silhouette Score of **0.5190**, but it classified **98 customers as noise**. This made it less suitable for the business goal, where each customer should ideally belong to a usable marketing segment.

Agglomerative Hierarchical Clustering achieved a Silhouette Score of **0.4201**.

Although DBSCAN performed better numerically, K-Means was selected as the final approach because it produced six practical customer groups and assigned all customers to a cluster.

## Cluster Interpretation and Business Value

The final clusters were profiled using customer age, income, and spending behavior. These profiles were interpreted as customer personas that can help the business understand different types of customers and create more relevant marketing campaigns.

This approach can support targeted promotions by reducing the chances of sending the same campaign to customers with very different purchasing behavior.

## Key Learning Outcomes

Through this task, I gained practical experience in:

* Applying unsupervised learning to a real dataset
* Building and evaluating K-Means clustering models
* Using the Elbow Method and Silhouette Score for cluster selection
* Applying DBSCAN and Hierarchical Clustering
* Understanding the importance of feature scaling
* Using PCA for cluster visualization
* Profiling and interpreting customer clusters
* Comparing technical results with practical business requirements

## Conclusion

This task showed that customer segmentation is not only about achieving the highest evaluation score. The final choice also depends on whether the clustering result is useful for the business problem. By comparing three different algorithms, K-Means was selected as the most practical solution for creating six actionable customer segments.

The task strengthened my understanding of unsupervised learning and demonstrated how clustering results can be converted into useful business insights.
