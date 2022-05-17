import cv2  #показание фото
img = cv2.imread("Pohtos/cat.jpg")

cv2.imshow("это кот", img)

cv2.waitKey(0)

import cv2

cap = cv2.VideoCapture(0)    # 0 1
cap.set(1, 500)
cap.set(4,500)



while True:
    success, img = cap.read()
    cv2.imshow("Resut", img)

    if cv2.waitKey(2) & 0xFF == ord("q"):
        break