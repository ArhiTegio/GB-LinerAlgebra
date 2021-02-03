import numpy as np
import scipy.spatial.distance
from numpy.linalg import norm



class LinerAlg:
    def Task2_2(self, v1:np.array, v2:np.array):
        a1 = norm(v1, ord=1)
        b2 = norm(v2, ord=1)
        return [[norm(v1, ord=1), norm(v2, ord=1)],
                [norm(v1, ord=2), norm(v2, ord=2)],
                [np.arccos(np.dot(v1, v2) / norm(v1) / norm(v2))]]

    def Task2_4(self, vectors:np.array):
        dist = scipy.spatial.distance.pdist(vectors, 'cosine')
        angle = np.rad2deg(np.arccos(1 - dist))
        return np.sum(angle)/len(angle) == 90