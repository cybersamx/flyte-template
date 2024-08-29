from flytekit import (
    task,
)
import pandas as pd
from sklearn.model_selection import (
    train_test_split,
)
from typing import Tuple

import project.core.data as data
import project.tasks as tasks


@task(container_image=tasks.image_spec)
def get_data() -> pd.DataFrame:
    return data.get_data()


@task(container_image=tasks.image_spec)
def split_to_train_test(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    x_data = data.get_x_data(df)
    y_data = data.get_y_data(df)
    return train_test_split(
        x_data,
        y_data,
        test_size=0.66,
        stratify=y_data,
        random_state=42,
    )
