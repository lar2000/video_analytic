import cv2

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

import imutils

import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img1 = cv2.imread("assets/img/1.jpg")

img = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)


# Adding custom options

custom_config = r'—oem 3—psm 6'

aa = pytesseract.image_to_string(img1, config=custom_config)

print(aa)

cv2.imshow('img1', img1)

cv2.waitKey(0)

cv2.destroyAllWindows()