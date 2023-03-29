import cv2
import numpy as np 
from matplotlib import pyplot as plt


img = cv2.imread('4.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)        
gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)     
blurred = cv2.bilateralFilter(gray,21,41,41)         
edged = cv2.Canny(blurred,400,600)        
thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 40)    


mask = cv2.bitwise_not(edged)    
thresh = cv2.bitwise_and(thresh,thresh,mask=mask)     
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))    
thresh = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel)    
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


output = img.copy()     
cv2.drawContours(output, contours, -1, (0,255,0), 1)    
plt.imshow(output)
plt.show()
cv2.waitKey(0)
