import cv2

cascade = cv2.CascadeClassifier('faces.xml')
video = cv2.VideoCapture(0)

while True:
    ret, img = video.read()
    faces = cascade.detectMultiScale(img, scaleFactor=1.5, minNeighbors=5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow('idontgetit', img)
    cv2.waitKey(30)

video.release()
cv2.destroyAllWindows()
