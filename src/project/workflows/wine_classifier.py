import pandas as pd
from flytekit import (
    workflow,
)
from typing import Tuple, Any

import project.tasks.preprocess as pp
import project.tasks.analyze as ana


@workflow
def classifier_wf() -> Tuple[Any, pd.Series, float, float]:
    # Get data.
    df = pp.get_data()
    x_train, x_test, y_train, y_test = pp.split_to_train_test(df)

    # Get the best classifier.
    best_params, clf = ana.get_classifier(x_train, y_train)

    # Metrics of the best classifier.
    features_score, train_acc, acc = ana.metrics(clf, x_train, x_test, y_train, y_test)

    return best_params, features_score, train_acc, acc


if __name__ == '__main__':
    print(f'running workflow {classifier_wf()}')
