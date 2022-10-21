from functools import reduce
from typing import Tuple

import numpy as np
import pandas as pd
from plotly.graph_objects import Figure
from scipy.stats import iqr
from sklearn.feature_selection import SelectKBest, chi2, f_classif
from sklearn.feature_selection import mutual_info_classif as mic


def _iqr_filter(df, feature):
    f_iqr = iqr(df[feature])
    upper_quant = f_iqr * 1.5 + df[feature].quantile(0.75)
    lower_quant = df[feature].quantile(0.25) - f_iqr * 1.5
    mask = (df[feature] < upper_quant) & (df[feature] > lower_quant)
    return mask


def _conjunction(arr: list[pd.Series]) -> pd.Series:
    return reduce(lambda x, y: x & y, arr)


def anomaly_values_filter(dataframe: pd.DataFrame, feature_list: list) -> pd.DataFrame:
    """Takes initial dataframe and drops anomalies by IQR.

    Args:
        dataframe (pd.DataFrame): initial dataframe.
        feature_list (str): list of features for anomaly detection.

    Returns:
        pd.DataFrame: prepared dataframe without anomaly values in numerical features.
    """
    all_mask = [_iqr_filter(dataframe, feature) for feature in feature_list]
    total_mask = _conjunction(all_mask)
    return dataframe[total_mask]


def extract_mutual_information(
    dataframe_prep: pd.DataFrame,
    target_df: pd.DataFrame,
    categorical_list: list,
    random: int,
) -> Tuple[Figure, list]:
    """Takes feature and target dataframes and conducts a mutual information test.

    Args:
        dataframe_prep (pd.DataFrame): prepared dataframe without anomalies.
        target_df (pd.DataFrame): dataframe with target feature.
        categorical_list (str): list of features for mutual information test.
        random (int): random_state value.

    Returns:
        Tuple: figure that reflects the distribution of feature importance and selected
        features as a result of a mutual information test.
    """
    importance_score = mic(
        dataframe_prep[categorical_list], target_df, random_state=random
    )
    features_importance = pd.Series(importance_score, categorical_list).sort_values(
        ascending=False
    )
    mutual_features = features_importance.index[:-2].tolist()
    plot = features_importance.plot(kind="barh", color="royalblue")
    return plot, mutual_features


def extract_chi2_information(
    dataframe_prep: pd.DataFrame, target_df: pd.DataFrame, categorical_list: list
) -> Tuple[Figure, list]:
    """Takes feature and target dataframes and conducts a chi2 information test.

    Args:
        dataframe_prep (pd.DataFrame): prepared dataframe without anomalies.
        target_df (pd.DataFrame): dataframe with target feature.
        categorical_list (str): list of features for chi2 information test.

    Returns:
        Tuple: figure that reflects the distribution of feature importance and selected
        features as a result of a chi2 information test.
    """
    chi2_test = SelectKBest(score_func=chi2, k=6)
    chi2_test.fit(dataframe_prep[categorical_list], target_df)
    features_importance = pd.Series(chi2_test.scores_, categorical_list).sort_values(
        ascending=False
    )
    chi2_scores_best = np.asarray(categorical_list)[chi2_test.get_support()].tolist()
    plot = features_importance.plot(kind="barh", color="royalblue")
    return plot, chi2_scores_best


def extract_anova_information(
    dataframe_prep: pd.DataFrame, target_df: pd.DataFrame, anova_list: list
) -> Tuple[Figure, list]:
    """Takes feature and target dataframes and conducts a chi2 information test.

    Args:
        dataframe_prep (pd.DataFrame): prepared dataframe without anomalies.
        target_df (pd.DataFrame): dataframe with target feature.
        mutual_list (str): list of features for chi2 information test.

    Returns:
        Tuple: figure that reflects the distribution of feature importance and selected
        features as a result of a anova information test.
    """
    anova_filter = SelectKBest(f_classif, k=4)
    anova_filter.fit(dataframe_prep[anova_list], target_df)
    features_importance = pd.Series(anova_filter.scores_, anova_list).sort_values(
        ascending=False
    )
    anova_scores_best = np.asarray(anova_list)[anova_filter.get_support()].tolist()
    plot = features_importance.plot(kind="barh", color="royalblue")
    return plot, anova_scores_best
