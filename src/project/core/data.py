import pandas as pd
from sklearn.datasets import load_wine


def get_data() -> pd.DataFrame:
    return load_wine(as_frame=True).frame


def get_x_data(df: pd.DataFrame) -> pd.DataFrame:
    # Return all columns but the target column as X.
    return df.drop(columns=['target'])


def get_y_data(df: pd.DataFrame) -> pd.DataFrame:
    # Get the data of target column only as y.
    return df[['target']]
