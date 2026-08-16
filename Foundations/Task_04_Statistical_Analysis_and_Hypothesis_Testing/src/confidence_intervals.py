import numpy as np
from scipy.stats import t


def mean_difference_ci(group1, group2, confidence=0.95):
    """
    Calculates a confidence interval for the difference
    between two independent group means using Welch's method.
    """
    group1 = np.asarray(group1)
    group2 = np.asarray(group2)

    mean_difference = np.mean(group1) - np.mean(group2)

    variance1 = np.var(group1, ddof=1)
    variance2 = np.var(group2, ddof=1)

    n1 = len(group1)
    n2 = len(group2)

    standard_error = np.sqrt(variance1 / n1 + variance2 / n2)

    degrees_of_freedom = (
        (variance1 / n1 + variance2 / n2) ** 2
        / (
            (variance1 / n1) ** 2 / (n1 - 1)
            + (variance2 / n2) ** 2 / (n2 - 1)
        )
    )

    alpha = 1 - confidence
    critical_value = t.ppf(1 - alpha / 2, degrees_of_freedom)

    margin_of_error = critical_value * standard_error

    lower = mean_difference - margin_of_error
    upper = mean_difference + margin_of_error

    return mean_difference, (lower, upper)
