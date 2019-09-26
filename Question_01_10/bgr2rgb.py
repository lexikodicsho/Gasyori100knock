import numpy as np
import cv2


def BGR2RGB(img):
    res = img.copy()

    return res[:, :, ::-1]


if __name__ == "__main__":

    img = cv2.imread("imori.jpg")

    img_bgr = BGR2RGB(img)

    cv2.imwrite("out.jpg", img_bgr)
    cv2.imshow("imori", img_bgr)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
