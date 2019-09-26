import numpy as np
import cv2


def BGR2GRAY(img):
    r = img[:, :, 2].copy()
    g = img[:, :, 1].copy()
    b = img[:, :, 0].copy()

    return 0.2126 * r + 0.7142 * g + 0.0722 * b


if __name__ == "__main__":

    img = cv2.imread("imori.jpg")

    gray = BGR2GRAY(img)

    cv2.imwrite("out.jpg", gray)
