# coding:utf-8
import numpy as np
import cv2


def BGR2GRAY(img):
    r = img[:, :, 2].copy()
    g = img[:, :, 1].copy()
    b = img[:, :, 0].copy()

    return 0.2126 * r + 0.7142 * g + 0.0722 * b


def otsu_binary(gray, th=127):
    res = gray.copy()
    w, h = res.shape[:2]

    max_sigma = 0
    max_t = 0

    for _t in range(1, 255):
        v0 = res[np.where(res < _t)]
        m0 = np.mean(v0) if len(v0) > 0 else 0.
        w0 = len(v0) / (h * w)
        v1 = res[np.where(res >= _t)]
        m1 = np.mean(v1) if len(v1) > 0 else 0.
        w1 = len(v1) / (h * w)
        sigma = w0 * w1 * ((m0 - m1) ** 2)
        if sigma > max_sigma:
            max_sigma = sigma
            max_t = _t

    print("threshold >>", max_t)
    th = max_t
    res[res < th] = 0
    res[res >= th] = 255

    return res


if __name__ == "__main__":

    img = cv2.imread("imori.jpg")
    gray = BGR2GRAY(img)

    binary = otsu_binary(gray)

    cv2.imwrite("out.jpg", binary)
