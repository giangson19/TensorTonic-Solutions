import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    
    return 0.0 if norm_a * norm_b == 0 else float (np.dot(a,b) / (norm_a * norm_b))