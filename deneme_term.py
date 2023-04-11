import cv2

image = cv2.imread('3.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

resized_image = cv2.resize(gray_image, (800, 600))

edges = cv2.Canny(resized_image, 100, 200)

contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

number_of_cars = 0
number_of_empty_parking_spots = 0

for contour in contours:
    area = cv2.contourArea(contour)
    if area > 100: # Burada "some_threshold" eşik değeri, tanımlamanız gereken bir değişken.
        number_of_cars += 1
    else:
        number_of_empty_parking_spots += 1

print("Number of cars: ", number_of_cars)
print("Number of empty parking spots: ", number_of_empty_parking_spots)
