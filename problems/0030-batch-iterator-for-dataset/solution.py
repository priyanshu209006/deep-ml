import numpy as np

def dont_know(X, batch_size=64):
    x2 = []
    n = X.shape[0]
    c = 0
    leng = (n + batch_size - 1) // batch_size

    for _ in range(leng):
        x1 = []
        for _ in range(batch_size):
            if c == n:
                break
            x1.append(X[c].tolist())
            c += 1
        x2.append(x1)

    return x2


def batch_iterator(X, y=None, batch_size=64):
    if y is None:
        return dont_know(X, batch_size)
    else:
        x2 = []
        for item1, item2 in zip(dont_know(X, batch_size),dont_know(y, batch_size)):
            x2.append([item1, [row for row in item2]])
        return x2