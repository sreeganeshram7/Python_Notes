# NOTE: numpy and pandas are already imported for you as:
# import numpy as np
# import pandas as pd
import numpy as np
def min_max_normalize(data: np.ndarray) -> np.ndarray:
    """
    Given a 1D NumPy array of integers, return a 1D NumPy array
    of floats where the values are normalized to the range [0, 1]
    using min-max normalization.

    The transformation is:
        x_i' = (x_i - min(data)) / (max(data) - min(data))

    Constraints:
    - 1 <= len(data) <= 10^4
    - 1 <= data[i] <= 10^4
    - Not all elements are the same.

    Parameters
    ----------
    data : np.ndarray
        1D array of integers.

    Returns
    -------
    np.ndarray
        1D array of floats with normalized values in [0, 1].
    """
    # TODO: implement your solution here
    data_min=data.min()
    data_max=data.max()
    return (data-data_min)/(data_max-data_min)