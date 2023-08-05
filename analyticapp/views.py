
import datetime
import time
import cv2

from django.shortcuts import render
from analyticapp.models import CCTV
# Create your views here.
from django.http import HttpResponse   

def index(request):
    all_data = CCTV.objects.all()
    return render(request, "cctv.html",{"all_data":all_data})
    
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
dt =datetime.datetime.now().strftime('%H%M%S')
video_cap = cv2.VideoWriter("vdo/myvdo" + dt + ".avi", fourcc,20.0,(640,480))

if not cap.isOpened():
   print("error opening camera")
   exit()
fps = 30.00
duration = 30 # seconds
frames = int(fps * duration)
start_time = time.time()
while(cap.isOpened()):
    check, frame = cap.read()
    
    if check==True:
        Datetime = str(datetime.datetime.now())
        cv2.putText(frame,"BesTech "+ Datetime,(10,30),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,0),cv2.LINE_4)
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

# video 