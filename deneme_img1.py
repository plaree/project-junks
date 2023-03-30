import cv2
import numpy as np


img = cv2.imread('3.jpg')


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


edges = cv2.Canny(gray, 50, 150)

lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=100, minLineLength=100, maxLineGap=10)


rectangles = []


for line in lines:
    x1, y1, x2, y2 = line[0]
    if abs(y2 - y1) < 5 and abs(x2 - x1) > 50:
        
        rect_x1 = min(x1, x2)
        rect_y1 = min(y1, y2)
        rect_x2 = max(x1, x2)
        rect_y2 = max(y1, y2)
       
        rectangles.append((rect_x1, rect_y1, rect_x2, rect_y2))


for rect in rectangles:
    cv2.rectangle(img, (rect[0], rect[1]), (rect[2], rect[3]), (0, 255, 0), 2)


cv2.imshow('result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()