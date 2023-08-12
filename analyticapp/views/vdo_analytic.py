import datetime
import time
import cv2

    
cap = cv2.VideoCapture("assets/video/suspens.mp4")
fourcc = cv2.VideoWriter_fourcc('H','2','6','4')
dt = datetime.datetime.now().strftime('%H%M%S')
video_cap = cv2.VideoWriter("assets/img/" + dt +".jpg", fourcc,20.0,(640,480))
   
fps = 30
duration = 10 # seconds
frames = int(fps * duration)

start_time = time.time()

while(cap.isOpened()):
    check, frame = cap.read()
    
    if check==True:
        Datetime = str(datetime.datetime.now())
        cv2.putText(frame,"BesTech "+ Datetime,(10,30),cv2.FONT_HERSHEY_SIMPLEX,0.9,(0,0,0),cv2.LINE_4)
        cv2.imshow('Output',frame)
        video_cap.write(frame)
        
        if cv2.waitKey(1) & 0xFF == ord('0'):
            break
        
        elapsed_time = time.time() - start_time
        if elapsed_time > duration:
            break

video_cap.release()
cap.release()
cv2.destroyAllWindows(), 