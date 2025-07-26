
import cv2
import numpy as np

def extract_big_road(image_path):
    img = cv2.imread(image_path)
    roi = img[60:260, 35:315]

    rows, cols = 6, 20
    cell_h = roi.shape[0] // rows
    cell_w = roi.shape[1] // cols

    results = []
    for col in range(cols):
        for row in range(rows):
            cell = roi[row*cell_h:(row+1)*cell_h, col*cell_w:(col+1)*cell_w]
            avg_color = np.mean(cell, axis=(0,1))
            b, g, r = avg_color

            if r > 150 and b < 100:
                results.append("B")
            elif b > 150 and r < 100:
                results.append("P")
    return results

def extract_secondary_patterns(image_path, roi_coords):
    img = cv2.imread(image_path)
    y1, y2, x1, x2 = roi_coords
    roi = img[y1:y2, x1:x2]

    rows, cols = 6, 20
    cell_h = roi.shape[0] // rows
    cell_w = roi.shape[1] // cols

    result = []
    for col in range(cols):
        for row in range(rows):
            cell = roi[row*cell_h:(row+1)*cell_h, col*cell_w:(col+1)*cell_w]
            avg_color = np.mean(cell, axis=(0,1))
            b, g, r = avg_color

            if r > 150 and b < 100:
                result.append('R')
            elif b > 150 and r < 100:
                result.append('B')
    return result
