# NOTE: numpy and pandas are already imported for you as:
# import numpy as np
# import pandas as pd
import pandas as pd
def replace_revenue_outliers(df: pd.DataFrame) -> pd.DataFrame:
    """
    Given a DataFrame with a 'Revenue' column, replace outlier values
    (values strictly greater than the 95th percentile) with the mean revenue.

    Steps:
    - Compute the mean of df['Revenue'].
    - Compute the 0.95 quantile (95th percentile) of df['Revenue'].
    - For all rows where Revenue > 95th percentile, replace Revenue with the mean.
    - Leave all other rows unchanged.

    Parameters
    ----------
    df : pd.DataFrame
        A DataFrame with a single column 'Revenue'.

    Returns
    -------
    pd.DataFrame
        A DataFrame where outliers in 'Revenue' are replaced by the mean.
    """
    # TODO: implement your solution here
    mean=df["Revenue"].mean()
    outlier=df["Revenue"].quantile(0.95)
    df["Revenue"]=df["Revenue"].apply(
        lambda x:mean if x>outlier else x
    )
    return df