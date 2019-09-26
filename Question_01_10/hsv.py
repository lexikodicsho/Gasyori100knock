import numpy as np


def RGB2HSV(img):

    norm = img / 255.

    v_max = np.max(norm, axis=-1)
    v_min = np.min(norm, axis=-1)
