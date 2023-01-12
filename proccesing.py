import cv2
import numpy as np


def segmentRows(inputFile, outputDir):
    img = cv2.imread(inputFile, flags=cv2.IMREAD_GRAYSCALE)
    binary = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 5, 1)
    cv2.imshow("orig", binary)
    columnHist = np.sum(binary, axis=1, keepdims=True) // 255
    columnHist = columnHist.flatten()
    lineHist = []
    rows = segmentByHist(columnHist, binary)
    for a in range(len(rows)):
        # cv2.imshow(f"{outputDir}/{int(a)}.png", rows[a])
        lineHist.append((np.sum(rows[a], axis=0, keepdims=True)//255).flatten())
    words = []
    s = 0
    f = 0
    for j in range(len(lineHist)):
        for i in range(3, len(lineHist[j]) - 3):
            if lineHist[j][i - 1] == 0 and lineHist[j][i - 2] == 0 and lineHist[j][i - 3] == 0 and lineHist[j][i] != 0:
                s = i
            if lineHist[j][i] != 0 and lineHist[j][i + 1] == 0 and lineHist[j][i + 2] == 0 and lineHist[j][i + 3] == 0:
                f = i + 1
                words.append(rows[j][:, s:f])
    # afisare cuvinte
    """i = 0
    for img in words:
        cv2.imshow(f"{i}", img)
        i += 1
        cv2.waitKey()"""


def segmentByHist(hist, original):
    segments = []
    s = 0
    f = 0
    for i in range(3, len(hist) - 3):
        if hist[i - 1] == 0 and hist[i - 2] == 0 and hist[i - 3] == 0 and hist[i] != 0:
            s = i
        if hist[i] != 0 and hist[i + 1] == 0 and hist[i + 2] == 0 and hist[i + 3] == 0:
            f = i + 1
            segments.append(original[s:f])
    return segments


if __name__ == "__main__":
    segmentRows("sample_text.png", "D:/AAA Facultate/AN 3 - SEM 1/PIM - Proiect/result_images")
