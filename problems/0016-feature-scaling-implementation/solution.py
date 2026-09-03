import numpy as np
import math

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):

    mean = []
    std = []
    standardized_data = np.zeros_like(data, dtype=float)

    rows = np.shape(data)[0]
    cols = np.shape(data)[1]

    for j in range(cols):
        total = 0
        for i in range(rows):
            total = total + data[i][j]
        mean.append(total / rows)

    for j in range(cols):
        sos = 0
        for i in range(rows):
            sos = sos + math.pow(data[i][j] - mean[j], 2)
        std.append(math.sqrt(sos / rows))

    for i in range(rows):
        for j in range(cols):
            standardized_data[i][j] = (data[i][j] - mean[j]) / std[j]

    min_val = [data[0][j] for j in range(cols)]
    max_val = [data[0][j] for j in range(cols)]

    for j in range(cols):
        for i in range(rows):
            if data[i][j] < min_val[j]:
                min_val[j] = data[i][j]

            if data[i][j] > max_val[j]:
                max_val[j] = data[i][j]

    normalized_data = np.zeros_like(data, dtype=float)

    for i in range(rows):
        for j in range(cols):
            normalized_data[i][j] = (data[i][j] - min_val[j]
            ) / (max_val[j] - min_val[j])

    return np.round(standardized_data, 4), np.round(normalized_data, 4)