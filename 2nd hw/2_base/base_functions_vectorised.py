import numpy as np

def select_elements_vectorized(X):
    X = np.array(X)
    selected_rows = X[::4]
    column_indices = np.arange(120, 500, 5)
    result = selected_rows[:, column_indices]
    return result
    
def sum_non_negative_diagonal_vectorized(X):
    X = np.array(X)
    diagonal = np.diagonal(X)
    non_negative_sum = np.sum(diagonal[diagonal >= 0])
    return non_negative_sum if np.any(diagonal >= 0) else -1
    
    
def replace_values_vectorized(X):
    X = np.array(X)
    column_means = np.mean(X, axis=0)
    mask = (X > 1.5 * column_means) | (X < 0.25 * column_means)
    X_copy = np.where(mask, -1, X)
    return X_copy
