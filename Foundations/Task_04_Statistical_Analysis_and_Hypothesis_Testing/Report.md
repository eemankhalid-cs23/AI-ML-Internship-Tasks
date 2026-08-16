# Task 04: Statistical Analysis and Hypothesis Testing

## 1. Objective

The objective of this task was to apply statistical analysis and hypothesis testing to medical insurance data and investigate whether smoking status, BMI, and region are associated with medical charges.

The main focus was on selecting suitable statistical tests, checking assumptions before applying them, interpreting p-values, and using effect sizes and confidence intervals to understand the practical importance of the results.

---

## 2. Dataset and Data Preparation

The Medical Cost Personal dataset was used for this analysis. It contains information about age, sex, BMI, number of children, smoking status, region, and medical insurance charges.

The `charges` column was used as the main outcome variable.

The dataset was first inspected for its dimensions, columns, data types, and duplicate records. One duplicate record was identified and removed before continuing with the analysis. Descriptive statistics were also calculated to understand the data before performing hypothesis tests.

---

## 3. Statistical Questions and Hypotheses

Three main questions were investigated:

### Question 1: Do smokers have higher medical charges than non-smokers?

- **H₀:** There is no significant difference in medical charges between smokers and non-smokers.
- **H₁:** There is a significant difference in medical charges between smokers and non-smokers.

### Question 2: Is BMI associated with medical charges?

- **H₀:** There is no significant relationship between BMI and medical charges.
- **H₁:** There is a significant relationship between BMI and medical charges.

### Question 3: Do medical charges differ across regions?

- **H₀:** There is no significant difference in medical charges among the regions.
- **H₁:** At least one region has a different mean medical charge.

---

## 4. Statistical Analysis

### 4.1 Smoking Status Analysis

The first analysis compared medical charges between smokers and non-smokers.

#### Levene's Test

Levene's test was used to check whether the variances of the two groups were equal.

- Test statistic: `332.4714`
- p-value: `1.67 × 10^-66`

Since the p-value was far below `0.05`, the equal-variance assumption was rejected. Therefore, Welch's t-test was selected because it is more appropriate when group variances are unequal.

#### Welch's t-test

- t-statistic: `32.7423`
- p-value: `6.26 × 10^-103`

The extremely small p-value provides strong evidence against the null hypothesis. Therefore, medical charges were significantly different between smokers and non-smokers.

#### Effect Size

Cohen's d was calculated to understand the size of the difference:

- **Cohen's d = `3.1603`**

This represents a very large effect, showing that the difference is practically important as well as statistically significant.

#### Mean Difference and Confidence Interval

The mean difference in charges was:

- **Mean difference = `$23,609.57`**

The 95% confidence interval was:

- **95% CI = [`$22,190.79`, `$25,028.35`]**

The interval does not include zero, which further supports the presence of a meaningful difference between the two groups.

#### Mann-Whitney U Test

A Mann-Whitney U test was also performed as a non-parametric comparison.

- U statistic: `283859.0`
- p-value: `5.75 × 10^-130`

The result was also highly significant, providing additional support for the difference between smokers and non-smokers.

---

### 4.2 BMI and Medical Charges

The relationship between BMI and medical charges was examined using both Pearson and Spearman correlation.

#### Pearson Correlation

- Correlation: `0.1984`
- p-value: `2.47 × 10^-13`
- 95% CI: `[0.1463, 0.2494]`

The positive correlation indicates that higher BMI tends to be associated with higher medical charges. However, the correlation is relatively weak.

#### Spearman Correlation

- Correlation: `0.1196`
- p-value: `1.16 × 10^-05`

Spearman correlation also showed a statistically significant positive relationship, but the correlation remained weak.

Overall, BMI has a statistically significant relationship with charges, but BMI alone does not explain a large amount of the variation in medical costs.

---

### 4.3 Regional Analysis

Medical charges were compared across four regions.

| Region | Count | Mean Charges | Median | Standard Deviation |
|---|---:|---:|---:|---:|
| Northeast | 324 | 13,406.38 | 11,255.80 | 10,057.65 |
| Northwest | 324 | 12,450.84 | 11,073.13 | 8,976.98 |
| Southeast | 364 | 14,735.41 | 13,971.10 | 9,294.13 |
| Southwest | 325 | 12,346.94 | 11,557.18 | 8,798.59 |

The Southeast had the highest average charges, while the Southwest had the lowest.

#### Levene's Test

- Test statistic: `5.5535`
- p-value: `0.000869`

The p-value was below `0.05`, indicating unequal variances across the regional groups. Therefore, Welch's ANOVA was used.

#### Welch's ANOVA

- Statistic: `2.5662`
- p-value: `0.05349`

The p-value was slightly above `0.05`. Therefore, there was not enough evidence to conclude that the mean medical charges differed significantly across regions at the 5% significance level.

#### Effect Size

Eta-squared was calculated:

- **η² = `0.00654`**

This represents a very small effect, suggesting that region explains only a small amount of the variation in medical charges.

#### Bonferroni Correction

Six pairwise regional comparisons were possible. To control the risk of false-positive results from multiple comparisons, Bonferroni correction was applied.

- Number of comparisons: `6`
- Adjusted significance level: `0.00833`

---

## 5. Key Findings

- Smoking status showed the strongest difference in medical charges.
- Smokers had substantially higher medical charges than non-smokers.
- The smoker/non-smoker difference had a very large effect size (`Cohen's d = 3.16`).
- The estimated mean difference was approximately `$23,609.57`.
- BMI had a statistically significant but weak positive relationship with medical charges.
- Regional differences in average charges were observed descriptively, but they were not statistically significant at the 5% level.
- Region also had a very small practical effect (`η² = 0.00654`).
- Using confidence intervals and effect sizes alongside p-values provided a better understanding of the practical meaning of the results.

---

## 6. Business Recommendations

Based on the analysis:

- Smoking status should receive particular attention when studying medical costs because smokers showed substantially higher charges.
- BMI can be considered as an additional factor, but its weak correlation suggests that it should not be treated as a strong standalone explanation of medical charges.
- Region should not be considered a major cost driver based on this analysis because its effect was small and the ANOVA result was not significant at the 5% level.
- Further analysis could examine multiple variables together, such as age, BMI, smoking status, and number of children, to better understand the factors contributing to medical charges.

---

## 7. Learning Outcomes

Through this task, I learned:

- How to formulate null and alternative hypotheses.
- How to select statistical tests according to the data and research question.
- Why assumptions such as equal variances should be checked before testing.
- When Welch's t-test is preferred over the standard independent t-test.
- How Mann-Whitney U provides a non-parametric alternative.
- The difference between Pearson and Spearman correlation.
- How Welch's ANOVA can be used when comparing multiple groups with unequal variances.
- How p-values indicate statistical significance.
- Why effect sizes are important for understanding practical significance.
- How confidence intervals provide a range of plausible estimates.
- Why Bonferroni correction is used for multiple comparisons.

---

## 8. Conclusion

This analysis showed a strong and practically important difference in medical charges between smokers and non-smokers. Both Welch's t-test and Mann-Whitney U test supported this finding, while the large Cohen's d showed that the difference was substantial.

BMI showed a statistically significant positive relationship with medical charges, but the relationship was relatively weak. Regional differences were visible in the descriptive statistics, but Welch's ANOVA did not provide sufficient evidence of a significant difference at the 5% level, and the effect size was very small.

Overall, the task helped me understand that statistical analysis involves more than calculating p-values. Checking assumptions, selecting the appropriate test, and using effect sizes and confidence intervals are important for reaching a more meaningful and reliable conclusion.
