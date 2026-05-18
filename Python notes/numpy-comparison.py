# student_template.py
# Do not change this import statement
import numpy as np
def array_comparison(a: np.ndarray, b: np.ndarray):
    """
    Compare two numpy arrays element-wise.
    
    Parameters:
    - a: NumPy array
    - b: NumPy array

    Returns:
    - equal: NumPy array of booleans (True where a == b)
    - greater: NumPy array of booleans (True where a > b)
    - less: NumPy array of booleans (True where a < b)
    """
    # TODO: Implement your logic here 
    equal = a==b
    greater= a>b
    less=a<b
    return equal,greater,less
