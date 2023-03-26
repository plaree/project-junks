import cv2
import numpy as np

# Resmi yükle
img = cv2.imread('3.jpg')

# Görüntüyü griye dönüştür
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Gürültüyü azaltmak için Gaussian bulanıklaştırma uygula
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Kenarları tespit etmek için Canny kenar algılama uygula
edges = cv2.Canny(blur, 50, 150)

# Daha iyi bir kontur algılama için morfolojik operasyonları uygula
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

# Tüm konturları bul
contours, hierarchy = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Konturları işle ve boş park alanlarını tespit et
parking_spaces = 0
for contour in contours:
    # Konturun alanını hesapla
    area = cv2.contourArea(contour)
    if area > 1000 and area < 10000:
        # Konturun çevresini bul
        perimeter = cv2.arcLength(contour, True)
        # Konturun yaklaşık bir çokgenle temsil edilmesi
        approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
        # Yaklaşık çokgenin köşe sayısını hesapla
        corners = len(approx)
        if corners == 4:
            # Bu bir dikdörtgen mi?
            x, y, w, h = cv2.boundingRect(contour)
            aspect_ratio = float(w) / h
            if aspect_ratio > 0.5 and aspect_ratio < 2:
                # Bu bir park alanı!
                parking_spaces += 1
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Sonuçları göster
cv2.imshow('result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
