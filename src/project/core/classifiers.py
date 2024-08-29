import math
import numpy as np
import pandas as pd
from sklearn.model_selection import (
    GridSearchCV,
)
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from typing import Any, Tuple


def best_rf_classifier(
    x_train: pd.DataFrame,
    y_train: pd.DataFrame,
) -> Tuple[Any, RandomForestClassifier]:
    params = {
        'max_depth': [10, 100, 1000],
        'max_features': [None, 'sqrt'],
        'n_estimators': [100, 1000, 2000]
    }

    gridsearch = GridSearchCV(
        estimator=RandomForestClassifier(random_state=42),
        param_grid=params,
        scoring='accuracy',
        n_jobs=-1,
        cv=5,
    )
    gridsearch.fit(x_train, y_train['target'])

    return gridsearch.best_params_, gridsearch.best_estimator_


def best_svm_classifier(
    x_train: pd.DataFrame,
    y_train: pd.DataFrame,
) -> Tuple[Any, SVC]:
    x = [math.pow(10, x) for x in range(0, 3)]
    y = np.arange(0.1, 1.0, 0.1)
    z = [2, 3, 4]

    params = [
        {'C': x, 'kernel': ['linear']},
        {'C': x, 'kernel': ['rbf'], 'gamma': y},
        {'C': x, 'kernel': ['poly'], 'gamma': y, 'degree': z}
    ]

    gridsearch = GridSearchCV(
        estimator=SVC(random_state=42),
        param_grid=params,
        scoring='accuracy',
        cv=10,
        n_jobs=-1,
    )
    gridsearch.fit(x_train, y_train['target'])

    return gridsearch.best_params_, gridsearch.best_estimator_
