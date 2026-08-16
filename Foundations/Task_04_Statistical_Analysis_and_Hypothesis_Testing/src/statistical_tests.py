from scipy.stats import ttest_ind, mannwhitneyu, f_oneway


def welch_t_test(group1, group2):
    """
    Performs Welch's independent samples t-test.
    Used when two groups have unequal variances.
    """
    return ttest_ind(group1, group2, equal_var=False)


def mann_whitney_test(group1, group2):
    """
    Performs a two-sided Mann-Whitney U test.
    Used as a non-parametric alternative for comparing two groups.
    """
    return mannwhitneyu(group1, group2, alternative="two-sided")


def welch_anova(*groups):
    """
    Performs Welch's ANOVA for comparing multiple groups
    when group variances are unequal.
    """
    return f_oneway(*groups, equal_var=False)
