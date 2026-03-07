import numpy as np

def bass_model(t, p, q, M):

    adopters = []
    cumulative = 0

    for i in range(len(t)):

        new_adopters = (p + q*(cumulative/M))*(M-cumulative)

        cumulative += new_adopters
        adopters.append(new_adopters)

    return np.array(adopters)