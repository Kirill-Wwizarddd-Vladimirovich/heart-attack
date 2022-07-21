import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pathlib
from pathlib import Path
sns.set(rc={'figure.figsize':(12,9)})


from .features import categorical_feat, numerical_feat

def info(dataframe: pd.DataFrame) -> dict:
    """Takes initial dataframe, returns multiple dataframes, that provides information about dataframe

    Args:
        dataframe (pd.DataFrame): initial dataframe with all data
        
    Returns:
        pd.DataFrame: new dataframes such as: df.info(), df.describe(), df.head()
    """
    df_info = pd.DataFrame({"name": dataframe.columns, "non-nulls": len(dataframe)-dataframe.isnull().sum().values, "nulls": dataframe.isnull().sum().values, "type": dataframe.dtypes.values})
    df_describe = dataframe.describe()
    df_head = dataframe.head()
    #df_list = [df_info, df_describe, df_head]
    df_dict = {'info': df_info, 'describe': df_describe, 'head': df_head}

    return df_dict

def hist_plots (dataframe: pd.DataFrame, dirname:Path):
    for feat in numerical_feat:
        data = pd.melt(dataframe, id_vars = ['output'])
        hist = sns.histplot(data[data['variable'] == feat], x = 'value', hue = 'output', kde = True);
        hist.axes.set_title(feat, fontsize = 14)
        plt.savefig(f"{dirname}/{feat}_hist.png")

def box_plots (dataframe: pd.DataFrame, dirname:Path):
    for feat in categorical_feat:
        data = pd.melt(dataframe, id_vars = ['output'])
        box = sns.boxplot( x = data['output'], y = data[data['variable'] == feat]['value']);
        box.axes.set_title(feat, fontsize = 14)
        plt.savefig(f"{dirname}/{feat}_box.png")

def heat_plot (dataframe: pd.DataFrame, dirname:Path): 
    sns.heatmap(dataframe.corr(), annot=True)
    plt.savefig(f"{dirname}/heatmap.png")
    
def pair_plot (dataframe: pd.DataFrame, dirname:Path): 
    sns.pairplot(dataframe[numerical_feat])
    plt.savefig(f"{dirname}/pairplot.png")