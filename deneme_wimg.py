import cv2

# Görüntüyü yükle
image = cv2.imread('cut.png')

# Görüntüyü gri tonlamalı olarak yükle
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Görüntüyü yeniden boyutlandır
#resized_image = cv2.resize(gray_image, (800, 600))

# Görüntüde kenarları tespit et
#edges = cv2.Canny(resized_image, 100, 200)
edges = cv2.Canny(image, 100, 250)


# Kenarları ve konturları tespit et
contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Konturları görüntüde göster
contour_image = image.copy()
cv2.drawContours(contour_image, contours, -1, (0, 0, 255), 2)
cv2.imshow('Contours', contour_image)
cv2.waitKey(0)

# Arabaları ve boş park yerlerini say
number_of_cars = 0
number_of_empty_parking_spots = 0

for contour in contours:
    area = cv2.contourArea(contour)
    if area > 333: # Eşik değerimizi burada 10000 piksel olarak varsaydık.
        number_of_cars += 1
        cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)
    else:
        number_of_empty_parking_spots += 1
        cv2.drawContours(image, [contour], -1, (255, 0, 0), 2)

# Sonuçları görüntü üzerinde göster
cv2.putText(image, "Number of cars: " + str(number_of_cars), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (102,51,51), 2)
cv2.putText(image, "Number of empty parking spots: " + str(number_of_empty_parking_spots), (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (102,51,51), 2)
cv2.imshow('Result', image)
cv2.waitKey(0)

cv2.destroyAllWindows()
