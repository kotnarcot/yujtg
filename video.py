import cv2
import pyttsx3
from time import sleep
engine = pyttsx3.init()
cap = cv2.VideoCapture(0)
z = 1000
while True:
    success, img = cap.read()
    cv2.imshow('Result', img)
    if z > 0:
        z = z-1
        gh = cv2.CascadeClassifier('frontface.xml')
        results = gh.detectMultiScale(img, scaleFactor=1.1, minNeighbors=6)
        for (x, y, w, h) in results:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), thickness=2)
            if x > 0:
                engine.say('Повернитесь боком')
                engine.runAndWait()
                z = 0
                x = 0
                y = 0
                w = 0
                h = 0
    if z == 0:
        while z > -1000:
            success, img = cap.read()
            cv2.imshow('Result', img)
            z = z - 1
            gh = cv2.CascadeClassifier('profile.xml')
            results = gh.detectMultiScale(img, scaleFactor=1.1, minNeighbors=7)
            for (x, y, w, h) in results:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), thickness=2)
                if x > 0:
                    engine.say('можете идти')
                    engine.runAndWait()
                    z = -1000
                    break
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    if z <= -999:
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


