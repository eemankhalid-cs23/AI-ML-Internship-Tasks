"""
Feature Selection Module
Task 3: Feature Engineering Mastery
"""

import pandas as pd

from sklearn.feature_selection import SelectKBest, mutual_info_regression


def select_features(X, y, k=192):
    """
    Select the top k features using mutual information.
    """
    selector = SelectKBest(
        score_func=mutual_info_regression,
        k=k
    )

    X_selected = selector.fit_transform(X, y)

    selected_features = X.columns[
        selector.get_support()
    ]

    return X_selected, selected_features, selector
