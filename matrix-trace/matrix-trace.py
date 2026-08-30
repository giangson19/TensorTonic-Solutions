import numpy as np

def matrix_trace(A: list) -> float:
    """
    Returns the trace as a float.
    """
    # Write code here
    sum = 0
    for i in range(len(A)):
        sum+= A[i][i] 

    return float(sum)