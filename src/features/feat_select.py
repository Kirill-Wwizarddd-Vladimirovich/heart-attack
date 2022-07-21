from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.metrics import classification_report
from sklearn.feature_selection import mutual_info_classif
from sklearn.svm import SVC
from sklearn.feature_selection import chi2
from sklearn.feature_selection import SelectKBest, f_classif
from pathlib import Path
import pandas as pd
import numpy as np

from src.data.features import categorical_feat, numerical_feat


def feat_target(dataframe: pd.DataFrame) -> dict:
    target = dataframe['output']
    features = dataframe.drop(columns = ['output'], axis = 1)
    df_dict = {'features': features, 'target': target}
    return df_dict



def mutual(dataframe: pd.DataFrame) -> pd.DataFrame:
    target = dataframe['output']
    features = dataframe.drop(columns = ['output'], axis = 1)
    importances = mutual_info_classif(features[categorical_feat], target)
    feat_importances = pd.Series(importances, features[categorical_feat].columns[0:len(dataframe.columns)-1])
    new = feat_importances.sort_values(ascending=False)
    mutual_feat = new.index[:-2]
    mutual_features = features[mutual_feat + numerical_feat]
    return mutual_features

def chi2(dataframe: pd.DataFrame):
    target = dataframe['output']
    features = dataframe.drop(columns = ['output'], axis = 1)
    chi2_test = SelectKBest(score_func=chi2, k=6)
    chi2_test.fit(features[categorical_feat], target)
    #?????chi2_scores = pd.DataFrame(list(zip(categorical_feat, chi2_test.scores_, chi2_test.pvalues_)), columns=['ftr', 'score', 'pval'])
    chi2_scores_best = np.asarray(categorical_feat)[chi2_test.get_support()]
    chi2_features = features[chi2_scores_best + numerical_feat]
    return chi2_features

def anova(dataframe: pd.DataFrame):
    target = dataframe['output']
    features = dataframe.drop(columns = ['output'], axis = 1)
    anova_filter = SelectKBest(f_classif, k=4)
    anova_filter.fit(features[numerical_feat], target)
    anova_scores_best = np.asarray(numerical_feat)[anova_filter.get_support()]
    #?????anova_results = pd.DataFrame(list(zip(numerical_feat, anova_filter.scores_, anova_filter.pvalues_)), columns=['ftr', 'score', 'pval'])
    anova_features = [anova_scores_best + categorical_feat]
    return anova_features