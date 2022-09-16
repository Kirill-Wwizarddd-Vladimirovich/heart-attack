from functools import reduce
from typing import Tuple

import numpy as np
import pandas as pd
from plotly.graph_objects import Figure
from sklearn.feature_selection import SelectKBest, chi2, f_classif
from sklearn.feature_selection import mutual_info_classif as mic


def _iqr_filter(df, feature):
    iqr = df[feature].quantile(0.75) - df[feature].quantile(0.25)
    upper_quant = iqr * 1.5 + df[feature].quantile(0.75)
    lower_quant = df[feature].quantile(0.25) - iqr * 1.5
    mask = (df[feature] < upper_quant) & (df[feature] > lower_quant)
    return mask


def _conjunction(arr: list[pd.Series]) -> pd.Series:
    return reduce(lambda x, y: x & y, arr)


def anomaly_values(dataframe: pd.DataFrame, feature_list: list) -> pd.DataFrame:
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


# можно ли сюда подавать Dynaconf
def mutual_information(
    dataframe_prep: pd.DataFrame,
    target_df: pd.DataFrame,
    mutual_list: list,
    random: int,
) -> Tuple[Figure, list]:
    """Takes feature and target dataframes and conducts a mutual information test.

    Args:
        dataframe_prep (pd.DataFrame): prepared dataframe without anomalies.
        target_df (pd.DataFrame): dataframe with target feature.
        mutual_list (str): list of features for mutual information test.
        random (int): random_state value.

    Returns:
        pd.DataFrame: prepared dataframe without anomaly values in numerical features.
    """
    importance_score = mic(dataframe_prep[mutual_list], target_df, random_state=random)
    features_importance = pd.Series(importance_score, mutual_list).sort_values(
        ascending=False
    )
    mutual_features = features_importance.index[:-2]
    plot = features_importance.plot(kind="barh", color="royalblue")
    return plot, mutual_features
