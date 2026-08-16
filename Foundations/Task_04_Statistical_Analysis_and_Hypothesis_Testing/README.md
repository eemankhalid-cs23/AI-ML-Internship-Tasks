# Task 04: Statistical Analysis and Hypothesis Testing

## Overview

In this task, I worked with the Medical Cost Personal dataset to understand which factors are related to medical insurance charges. The main focus was not only to calculate statistics, but also to understand why a particular statistical test should be used and how its result should be interpreted.

I focused on three questions:

- Do smokers have higher medical charges than non-smokers?
- Is BMI related to medical charges?
- Do medical charges differ across regions?

## Dataset

The dataset contains information about individuals including:

- Age
- Sex
- BMI
- Number of children
- Smoking status
- Region
- Medical charges

The `charges` column was used as the main variable for the statistical analysis.

## What I Did

I first inspected the dataset, checked its structure and descriptive statistics, and handled the duplicate record found in the data.

After understanding the data, I formulated statistical questions and their null and alternative hypotheses. Before applying tests, I also checked assumptions such as equality of variances.

Different statistical methods were then selected according to the type of question and the characteristics of the data.

### Statistical Methods Used

- Levene's Test — to check equality of variances
- Welch's t-test — to compare charges between smokers and non-smokers when variances were unequal
- Mann-Whitney U Test — to provide a non-parametric comparison between the two groups
- Pearson Correlation — to examine the linear relationship between BMI and charges
- Spearman Correlation — to examine the monotonic relationship between BMI and charges
- Welch's ANOVA — to compare charges across regions with unequal variances
- Cohen's d — to measure the size of the difference between smokers and non-smokers
- Eta-squared — to measure the practical effect of region
- Confidence Interval — to estimate the range of the smoker/non-smoker mean difference
- Bonferroni correction — to control the significance level when making multiple pairwise comparisons

## Main Findings

The strongest difference was found between smokers and non-smokers. The average medical charge for smokers was substantially higher, and the effect size was very large.

BMI showed a statistically significant relationship with medical charges, but the correlation was relatively weak.

For region, the average charges were somewhat different, but Welch's ANOVA did not provide enough evidence to conclude that the regional differences were statistically significant at the 5% level. The effect size was also very small.

## Project Structure

```text
Task_04_Statistical_Analysis_and_Hypothesis_Testing/
│
├── data/
│   └── medical_cost_personal.csv
│
├── notebooks/
│   └── Task_04_Statistical_Analysis_and_Hypothesis_Testing.ipynb
│
├── src/
│   ├── statistical_tests.py
│   ├── effect_sizes.py
│   └── confidence_intervals.py
│
├── reports/
│   └── Task_04_Report.md
│
├── README.md
└── requirements.txt
## Tools Used

Python, Pandas, NumPy, SciPy, Matplotlib, Seaborn and Google Colab.

## Conclusion

This task helped me understand that choosing a statistical test depends on the data and the question being investigated. I also learned that a very small p-value does not by itself tell us how important a result is, so effect sizes and confidence intervals are useful for understanding the practical meaning of the results.
