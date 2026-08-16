import numpy as np


def cohens_d(group1, group2):
    """
    Calculates Cohen's d for the difference between two groups.
    """
    group1 = np.asarray(group1)
    group2 = np.asarray(group2)

    n1 = len(group1)
    n2 = len(group2)

    pooled_std = np.sqrt(
        ((n1 - 1) * np.var(group1, ddof=1) +
         (n2 - 1) * np.var(group2, ddof=1))
        / (n1 + n2 - 2)
    )

    return (np.mean(group1) - np.mean(group2)) / pooled_std


def eta_squared(groups):
    """
    Calculates eta-squared as an effect size for group differences.
    """
    groups = [np.asarray(group) for group in groups]

    all_values = np.concatenate(groups)
    grand_mean = np.mean(all_values)

    between_group = sum(
        len(group) * (np.mean(group) - grand_mean) ** 2
        for group in groups
    )

    total = np.sum((all_values - grand_mean) ** 2)

    return between_group / total
