"""
Feature Engineering Module
Task 3: Feature Engineering Mastery
"""

import pandas as pd
import numpy as np


def create_engineered_features(df):
    """
    Create and return engineered features for the House Prices dataset.
    """
    df = df.copy()

    # Numerical feature transformations
    numerical_columns = df.select_dtypes(
        include=np.number
    ).columns

    for column in numerical_columns:
        if column != "SalePrice":
            df[column] = df[column].fillna(df[column].median())

    return df
