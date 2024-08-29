from flytekit import (
    task,
)
import pandas as pd
from sklearn.metrics import accuracy_score
from typing import Tuple, Any

import project.core.classifiers as cl
from project.tasks import image_spec


@task(container_image=image_spec)
def get_classifier(
    x_train: pd.DataFrame,
    y_train: pd.DataFrame,
) -> tuple[Any, Any]:
    best_params, clf = cl.best_rf_classifier(x_train, y_train)

    return best_params, clf


@task(container_image=image_spec)
def metrics(
    clf: Any,
    x_train: pd.DataFrame,
    x_test: pd.DataFrame,
    y_train: pd.DataFrame,
    y_test: pd.DataFrame,
) -> Tuple[pd.Series, float, float]:
    train_acc = clf.score(x_train, y_train)

    y_pred = clf.predict(x_test)
    acc = accuracy_score(y_test, y_pred)

    feature_scores = (pd.Series(clf.feature_importances_, index=x_train.columns).
                      sort_values(ascending=False))

    return feature_scores, train_acc, acc
