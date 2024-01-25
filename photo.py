import cv2

img = cv2.imread('images/photo1705566709.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = cv2.CascadeClassifier('faces.xml')

res = faces.detectMultiScale(gray, scaleFactor=4, minNeighbors=3)

for (x, y, w, h) in res:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), thickness=3)

cv2.imshow("Result", img)
cv2.waitKey(0)