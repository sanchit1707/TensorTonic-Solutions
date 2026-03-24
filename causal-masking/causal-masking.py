import numpy as np

def apply_causal_mask(scores, mask_value=-1e9):
    """
    scores: np.ndarray with shape (..., T, T)
    mask_value: float used to mask future positions (e.g., -1e9)
    Return: masked scores (same shape, dtype=float)
    """
    t=scores.shape[-1] 
    
    mask=np.triu(np.ones((t,t)),k=1) 

    return np.where(mask, mask_value, scores.astype(float))
    
    pass