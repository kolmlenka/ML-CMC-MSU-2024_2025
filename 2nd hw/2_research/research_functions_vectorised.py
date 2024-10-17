import numpy as np


#НЕ ВСЕ ФУНКЦИИ РАБОТАЮТ КОРРЕКТНО!!!! НА 2ой ВЫЛЕЗАЕТ "Wrong answer on test 0", НА 5ой ВЫЛЕЗАЕТ RE


def are_multisets_equal(x: np.ndarray, y: np.ndarray) -> bool:
    unique_x, counts_x = np.unique(x, return_counts=True)
    unique_y, counts_y = np.unique(y, return_counts=True)
    return np.array_equal(unique_x, unique_y) and np.array_equal(counts_x, counts_y)


def max_prod_mod_3(x: np.ndarray) -> int:
    if len(x) == 0:
        return -1
    shifted_x = np.roll(x, -1)
    products = x * shifted_x
    mask = (x % 3 == 0) | (shifted_x % 3 == 0)
    if np.any(mask):
        max_product = np.max(products[mask])
        return max_product
    else:
        return -1


def convert_image(image: np.ndarray, weights: np.ndarray) -> np.ndarray:
    result = np.tensordot(image, weights, axes=(2, 0))
    return result


def rle_scalar(x: np.ndarray, y: np.ndarray) -> int:
    x_dec = np.concatenate([np.full(count, value) for value, count in x])
    y_dec = np.concatenate([np.full(count, value) for value, count in y])
    if x_dec.size != y_dec.size:
        result = -1
    else:
        result = np.dot(x_dec, y_dec)
    return result


def cosine_distance(X: np.ndarray, Y: np.ndarray) -> np.ndarray:
    norm_X = np.linalg.norm(X, axis=1, keepdims=True)
    norm_Y = np.linalg.norm(Y, axis=1, keepdims=True)
    dot_product = X @ Y.T
    norm_X[norm_X == 0] = 1
    norm_Y[norm_Y == 0] = 1
    cosine_similarity = dot_product / (norm_X @ norm_Y.T)
    M = 1 - cosine_similarity
    M[(norm_X == 1) | (norm_Y == 1)] = 1
    return M
