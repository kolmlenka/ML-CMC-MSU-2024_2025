def select_elements(X):
    result = []
    for i in range(0, len(X), 4):
        temp = []
        for j in range(120, 500, 5):
            temp.append(X[i][j])
        result.append(temp)
    return result

def sum_non_negative_diagonal(X):
    total_sum = 0
    has_non_negative = False
    for i in range(min(len(X), len(X[0]))):
        if X[i][i] >= 0:
            total_sum += X[i][i]
            has_non_negative = True      
    return total_sum if has_non_negative else -1
    
from copy import deepcopy

def replace_values(X):
    X_copy = deepcopy(X)
    n = len(X)
    m = len(X[0])
    column_means = [sum(X[i][j] for i in range(n)) / n for j in range(m)]
    for j in range(m):
        mean = column_means[j]
        for i in range(n):
            if X_copy[i][j] > 1.5 * mean or X_copy[i][j] < 0.25 * mean:
                X_copy[i][j] = -1     
    return X_copy
