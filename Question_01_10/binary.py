import numpy as np
import cv2

from bgr2gray import BGR2GRAY


def binary(gray, th=128):
    res = gray.copy()

    res = np.where(gray < th, 0, 255)

    return res


if __name__ == "__main__":

    img = cv2.imread("imori.jpg")

    gray = BGR2GRAY(img)
    binary = binary(gray)

    cv2.imwrite("out.jpg", binary)
