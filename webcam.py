import cv2
frameWidth = 640
frameHeight = 480
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)

while True:
    success , img= cap.read()
    if success==False:
        break
    imgResize = cv2.resize(img, (500,400))
    imgGray = cv2.cvtColor(imgResize, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgResize, 1.1, 4)
    for (x, y, w, h) in faces:
        print(imgGray)
        cv2.rectangle(imgResize, (x, y), (x + w, y + h), (255, 255, 255), 2)
    cv2.imshow('Result', imgResize)
    
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
