

import pandas as pd
import numpy as np
from pathlib import Path


def descriptive_statistics(df:pd.DataFrame) -> pd.DataFrame:
    """
    Calculates descriptive statistics for the dataset.

    Args:
       df:
            A pandas DataFrame containing a numeric dataset.

    Raises:
        TypeError:
            If the input is not a Pandas Dataframe
        ValueError:
            If the Pandas DataFrame is empty.

    Returns:
        A pandas DataFrame with the following values:
            observations:
                Provides the number of observations in the dataset
            mean
                Arithmetic mean of the data
            median
                The median (middle) value in the dataset
            minimum
                The minimum value in the dataset
            maximum
                The maximum value in the dataset
            range
                The difference between the maximum and minimum.
            variance
                Average of the squared distances of the observations from the mean.
            std_dev
                The standard deviation, which is the square root of the variance.
    """
    # Error Handling
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Passed argument must be a pandas DataFrame.")

    if df.empty:
        raise ValueError("DataFrame must contain values.")

    # Extract the relevant column for analysis
    flow = df["peak_flow_cfs"]

    summary = {
        "observations": len(flow),
        "mean": flow.mean(),
        "median": flow.median(),
        "minimum": flow.min(),
        "maximum": flow.max(),
        "range": flow.max() - flow.min(),
        "variance": flow.var(),
        "std_dev": flow.std(),
    }

    return pd.DataFrame([summary])
