import cv2


img = cv2.imread("1.jpg")


gh = cv2.CascadeClassifier("gh.xml")
results = gh.detectMultiScale(img, scaleFactor =4, minNeighbors = 44 ) #вместо (a-scaleFactor малое число), вместо (a-minNeighbors любое число)


print(results)

for (x,y,w,h) in results:
    cv2.rectangle(img, (x,y),(x+w, y+h), (0,0,255),thickness= 2)

cv2.imshow("Result",img)
cv2.waitKey(0)