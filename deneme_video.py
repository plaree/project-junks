import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)
    lines = cv2.HoughLinesP(edges, 1, cv2.PI/180, 100, minLineLength=100, maxLineGap=10)
    
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        
    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()