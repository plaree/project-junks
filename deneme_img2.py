import cv2
import numpy as np


img = cv2.imread('3.jpg')


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


blur = cv2.GaussianBlur(gray, (5, 5), 0)

edges = cv2.Canny(blur, 50, 150)


kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)


contours, hierarchy = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


parking_spaces = 0
for contour in contours:
    
    area = cv2.contourArea(contour)
    if area > 1000 and area < 10000:
      
        perimeter = cv2.arcLength(contour, True)
     
        approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
       
        corners = len(approx)
        if corners == 4:
         
            x, y, w, h = cv2.boundingRect(contour)
            aspect_ratio = float(w) / h
            if aspect_ratio > 0.5 and aspect_ratio < 2:
                
                parking_spaces += 1
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)


cv2.imshow('result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
