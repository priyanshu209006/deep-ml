import numpy as np

def to_categorical(x, n_col=None):
    classes = np.unique(x)

    if n_col is None:
        n_col = len(classes)

    encoding = np.zeros((len(x), n_col))

    for i in range(len(x)):
        encoding[i][x[i]] = 1

    return encoding