from collections import Counter
from typing import List


#НЕ ВСЕ ФУНКЦИИ ВЕРНЫЕ, 5ая ВЫДАЕТ ОШИБКУ RE


def are_multisets_equal(x: List[int], y: List[int]) -> bool:
    count_x = {}
    count_y = {}
    for item in x:
        count_x[item] = count_x.get(item, 0) + 1
    for item in y:
        count_y[item] = count_y.get(item, 0) + 1
    return count_x == count_y


def max_prod_mod_3(x: List[int]) -> int:
    max_product = -1
    for i in range(len(x) - 1):
        if x[i] % 3 == 0 or x[i + 1] % 3 == 0:
            product = x[i] * x[i + 1]
            if product > max_product:
                max_product = product
    return max_product


def convert_image(image: List[List[List[float]]], weights: List[float]) -> List[List[float]]:
    height = len(image)
    width = len(image[0])
    num_channels = len(weights)
    result = [[0] * width for _ in range(height)]
    for h in range(height):
        for w in range(width):
            pixel_sum = 0
            for c in range(num_channels):
                pixel_sum += image[h][w][c] * weights[c]
            result[h][w] = pixel_sum
            
    return result


def rle_scalar(x: List[List[int]], y: List[List[int]]) -> int:
    x_dec = []
    for value, count in x:
        x_dec.extend([value] * count)
    y_dec = []
    for value, count in y:
        y_dec.extend([value] * count)
    
    if len(x_dec) != len(y_dec):
        result = -1
    else:
        result = sum(x_dec[i] * y_dec[i] for i in range(len(x_dec)))
    
    return result


def cosine_distance(X: List[List[float]], Y: List[List[float]]) -> List[List[float]]:
    n = len(X)
    m = len(Y)
    if n == 0 or m == 0 or len(X[0]) != len(Y[0]):
        raise ValueError("Input matrices must have the same number of columns and cannot be empty.")
    
    M = [[0] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            dot_product = sum(X[i][k] * Y[j][k] for k in range(len(X[0])))
            norm_x = math.sqrt(sum(X[i][k] ** 2 for k in range(len(X[0]))))
            norm_y = math.sqrt(sum(Y[j][k] ** 2 for k in range(len(Y[0]))))
            
            if norm_x == 0 or norm_y == 0:
                M[i][j] = 1
            else:
                M[i][j] = 1 - (dot_product / (norm_x * norm_y))
    
    return M

