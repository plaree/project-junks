import cv2

# Görüntüyü yükle
image = cv2.imread('4.png')

# Görüntüyü gri tonlamalı olarak yükle
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Görüntüyü yeniden boyutlandır
resized_image = cv2.resize(gray_image, (800, 600))

# Görüntüyü blurlaştır (daha pürüzsüz hale getirir)
blurred_image = cv2.GaussianBlur(resized_image, (5, 5), 0)

# Görüntüyü binary (siyah/beyaz) hale getir
_, threshold_image = cv2.threshold(blurred_image, 100, 255, cv2.THRESH_BINARY_INV)

# Contours'ları tespit et
contours, _ = cv2.findContours(threshold_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Arabaların konturlarını tespit et
car_contours = []

for contour in contours:
    # Konturun alanını hesapla
    area = cv2.contourArea(contour)
    # Eğer konturun alanı, belirli bir değerin üzerindeyse, araç olarak kabul et
    if area > 500 and area < 5000:
        # Konturu elips şekline yakın bir şekilde yaklaştır
        ellipse = cv2.fitEllipse(contour)
        # Konturu elips şekline dönüştür
        car_contours.append(ellipse)
        # Elips çiz
        cv2.ellipse(image, ellipse, (0, 255, 0), 2)

# Arabaların sayısını ve konturlarını göster
number_of_cars = len(car_contours)
print("Number of cars: ", number_of_cars)
cv2.imshow('Result', image)
cv2.waitKey(0)

cv2.destroyAllWindows()
