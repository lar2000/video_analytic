import cv2
import numpy as np
import matplotlib.pyplot as plt

path = "assets/img/3335.jpg"
mpt = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_russian_plate_number.xml")
count = 0
minArea = 1000

while True:
    
    img = cv2.imread(path)
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    numberplate = mpt.detectMultiScale(imgGray,1.1, 4)

    for (x, y, w, h) in numberplate:
        area = w*h
    
    if area > minArea:
       cv2.rectangle(img, (x, y+10), (x+w-30, y+h+50), (0,0,255),2)
       cv2.putText(img, "Numberplate",(x,y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,0),2)
       imgRoi = img[y:y+h+50, x:x+w-30]
       
    cv2.imshow("ROI",imgRoi)
    cv2.imshow("orginal",img)
    if cv2.waitKey(0) & 0xFF == ord('1'):
        cv2.imwrite("Detected_img" +str(count)+".jpg",imgRoi)
        cv2.putText(img,"saved", (40,40),cv2.FONT_HERSHEY_DUPLEX,2, (0,255,255),2)

    cv2.destroyAllWindows()