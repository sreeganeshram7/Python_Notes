# NOTE: numpy and pandas are already imported for you as:
# import numpy as np
# import pandas as pd
import pandas as pd
def remove_duplicate_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Given a DataFrame with columns "Name" and "Age",
    return a DataFrame where duplicate names are removed,
    keeping only the first occurrence of each name.

    Parameters:
    - df: pd.DataFrame with columns:
        - "Name": string
        - "Age": int

    Returns:
    - pd.DataFrame with only the first occurrence of each unique "Name",
      in the same relative order as the input.
    """
    # TODO: implement your solution here
    return df.drop_duplicates(subset="Name",keep="First")
