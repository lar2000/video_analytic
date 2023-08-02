import datetime
from django.shortcuts import render
from analyticapp.models import CCTV
import cv2

# Create your views here.
from django.http import HttpResponse   

#def index(request):
    #return HttpResponse("My Word ")
    
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
video_cap = cv2.VideoWriter("Output.avi", fourcc,20.0,(640,480))
fps = 30.00
duration = 60 # seconds
frames = int(fps * duration)

while(cap.isOpened()):
    check, frame = cap.read()
    
    if check==True:
        Datetime = str(datetime.datetime.now())
        cv2.putText(frame,"BesTech "+Datetime,(10,30),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,0),cv2.LINE_4)
        cv2.imshow('Output',frame)
        video_cap.write(frame)

        if cv2.waitKey(1) & 0xFF == ord('0'):
            break

video_cap.release()
cap.release()
cv2.destroyAllWindows(), 

    
def index(request):
    all_data = CCTV.objects.all()
    return render(request, "cctv.html",{"all_data":all_data})
    