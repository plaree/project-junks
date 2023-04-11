import cv2

# Görüntüyü yükle
image = cv2.imread('3.jpg')

# Görüntüyü gri tonlamalı olarak yükle
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Görüntüyü yeniden boyutlandır
#resized_image = cv2.resize(gray_image, (800, 600))

# Görüntüde kenarları tespit et
edges = cv2.Canny(image, 100, 200)

# Kenarları ve konturları tespit et
contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Arabaları say
number_of_cars = 0

for contour in contours:
    area = cv2.contourArea(contour)
    if area > 100: # Eşik değerimizi burada 10000 piksel olarak varsaydık.
        number_of_cars += 1
        cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)

# Sonuçları görüntü üzerinde göster
cv2.putText(image, "Number of cars: " + str(number_of_cars), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)
cv2.imshow('Result', image)
cv2.waitKey(0)

cv2.destroyAllWindows()
