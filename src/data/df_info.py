import pandas as pd
import seaborn as sns
from plotly.graph_objects import Figure

sns.set(rc={"figure.figsize": (12, 9)})  # noqa: E402


def hist_plots(dataframe: pd.DataFrame, feature: str) -> Figure:
    """Takes initial dataframe and creates histogram.

    Args:
        dataframe (pd.DataFrame): initial dataframe.
        feature (str): for creating histogram.

    Returns:
        Figure: histograms that reflect distribution of a feature for target variables.
    """
    data = pd.melt(dataframe, id_vars=["output"])
    hist = sns.histplot(
        data[data["variable"] == feature], x="value", hue="output", kde=True
    )
    hist.axes.set_title(feature, fontsize=14)
    return hist


def box_plots(dataframe: pd.DataFrame, feature: str) -> Figure:
    """Takes initial dataframe and creates figures.

    Args:
        dataframe (pd.DataFrame): initial dataframe.
        feature (str): for creating figure.

    Returns:
        Figure: box plots that reflect distribution of a feature for target variables.
    """
    data = pd.melt(dataframe, id_vars=["output"])
    data_plot = data[data["variable"] == feature]["value"]
    box = sns.boxplot(x=data["output"], y=data_plot)
    box.axes.set_title(feature, fontsize=14)
    return box


def count_plots(dataframe: pd.DataFrame, feature: str) -> Figure:
    """Takes initial dataframe and creates figures.

    Args:
        dataframe (pd.DataFrame): initial dataframe.
        feature (str): for creating figure.

    Returns:
        Figure: counts plots that reflect distribution of a feature.
    """
    data = dataframe[feature]
    count = sns.countplot(data)
    count.axes.set_title(feature, fontsize=14)
    return count


def heat_plot(dataframe: pd.DataFrame) -> Figure:
    """Takes initial dataframe and creates heatmap plot.

    Args:
        dataframe (pd.DataFrame): initial dataframe.

    Returns:
        Figure: heatmap plot for all features.
    """
    heatmap = sns.heatmap(dataframe.corr(), annot=True)
    return heatmap


def pair_plot(dataframe: pd.DataFrame, feat_list: list) -> Figure:
    """Takes initial dataframe and creates pair plots for numerical features.

    Args:
        dataframe (pd.DataFrame): initial dataframe
        feat_list (list): list of numerical features
    Returns:
        Figure: united figure with all pair plots for numerical features.
    """
    pairplot = sns.pairplot(dataframe[feat_list])
    return pairplot
