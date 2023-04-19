import cv2

# Cascade sınıflandırıcısı yüklenir
car_cascade = cv2.CascadeClassifier('denemeler/cars.xml')

# Görüntü okunur
img = cv2.imread('4.png')

# Görüntü grayscale olarak dönüştürülür
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Araçlar tespit edilir
cars = car_cascade.detectMultiScale(gray, 0.5, 1.1)

# Her bir araç için dikdörtgen çizilir
for (x, y, w, h) in cars:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

# Sonuç görüntüsü gösterilir
cv2.imshow('Cars Detected', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
