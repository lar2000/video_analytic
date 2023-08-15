import datetime
import cv2
import time
cap = cv2.VideoCapture('assets/video/suspens.mp4')  #Path to footage
car_cascade = cv2.CascadeClassifier('packages/hand.xml') 
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
dt = datetime.datetime.now().strftime('%H%M%S')#Path to cars.xml


#Coordinates of polygon in frame::: [[x1,y1],[x2,y2],[x3,y3],[x4,y4]]
coord=[[480,500],[825,500],[430,710],[890,710]]

#Distance between two horizontal lines in (meter)
dist = 3

border_x1, border_y1 = 480, 500
border_x2, border_y2 = 825, 710

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    Datetime = str(datetime.datetime.now())
    cv2.putText(img, "BesTech " + Datetime, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 0), cv2.LINE_4)
    cars = car_cascade.detectMultiScale(gray,1.2,2)
    video_cap = cv2.VideoWriter("assets/img/" + dt +".jpg", fourcc,20.0,(640,480))

    for (x,y,w,h) in cars:
        cv2.rectangle(img,(x,y),(x+w,y+h),(225,0,0),2)
        
        # Check if car intersects with red border
        if x + w >= border_x1 and x <= border_x2 and y + h >= border_y1 and y <= border_y2:
            cv2.rectangle(img,(border_x1,border_y1),(border_x2,border_y2),(0,0,255),2) # Draw red border
            video_cap.write(img) # Start recording video

    cv2.line(img, (coord[0][0],coord[0][1]),(coord[1][0],coord[1][1]),(0,0,255),2)   #First horizontal line
    cv2.line(img, (coord[0][0],coord[0][1]), (coord[2][0],coord[2][1]), (0, 0, 255), 2) #Vertical left line
    cv2.line(img, (coord[2][0],coord[2][1]), (coord[3][0], coord[3][1]), (0, 0, 255), 2) #Second horizontal line
    cv2.line(img, (coord[1][0],coord[1][1]), (coord[3][0], coord[3][1]), (0, 0, 255), 2) #Vertical right line
    
    cv2.imshow('img',img) #Shows the frame

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()