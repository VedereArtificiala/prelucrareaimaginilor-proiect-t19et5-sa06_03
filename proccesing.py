import cv2
import numpy as np


def segmentRows(inputFile, outputDir):
    img = cv2.imread(inputFile, flags=cv2.IMREAD_GRAYSCALE)
    binary = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 5, 1)
    hh = np.sum(binary, axis=1, keepdims=True) // 255
    rows = []
    s = 0
    f = 0
    ind = 0
    for i in range(3, len(hh.flatten())-3):
        if hh[i-1] == 0 and hh[i-2] == 0 and hh[i-3] == 0 and hh[i] != 0:
            s = i
        if hh[i] != 0 and hh[i+1] == 0 and hh[i+2] == 0 and hh[i+3] == 0:
            f = i + 1
            rows.append(binary[s:f])
            ind += 1
    for a in range(ind):
        cv2.imwrite(f"{outputDir}/{int(a)}.png", rows[a])
