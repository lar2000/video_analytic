import cv2
import numpy as np
import matplotlib.pyplot as plt
import pytesseract
from PIL import Image, ImageGrab
pytesseract.pytesseract.tesseract_txt = r'D:\Django'
#print(pytesseract.image_to_string(r'C:\Users\Deen\Desktop\testocr\tess.png'))

def convertImage(image): #ฟังก์แปลงค่าสี
    gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY) #แปลงภาพเป็นเกรย์สเกล
    blur = cv2.GaussianBlur(gray,(5,5),0) #การเลอภาพ
    canny = cv2.Canny(blur,100,200) #ฟังก์แปรงภาพเดป็นขาว-ดำ
    return canny 

img = cv2.imread("assets/img/3093.jpg") #ส่งภาพไปยังฟังก์ชั่นก่อนหน้า
processed_img = convertImage(img)
original_img = img.copy() #สร้างตัวแปรเพื่อที่จะไปตัด

contour_img = processed_img.copy() #การกอปปี้ภาพ

contours, heirarchy = cv2.findContours(contour_img,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE) #contour การหาเส็นคอบ บรรทัดการหา
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10] #การ sort contour แค่ 10 ตัวที่สมบูรที่สุด

for contour in contours: #การแตกcontour 
    p = cv2.arcLength(contour,True)
    approx = cv2.approxPolyDP(contour,0.02*p,True) #การมองให้มันเป็นมุม

    if len(approx) == 4: #ถ้าcontour ที่แตกออกมี 4 มุมจะเข้าอีฟนี้
        
        x,y,w,h = cv2.boundingRect(contour) #การแตกcontour ค่าเป็น แกน x y 
        license_img = original_img[y:y+h,x:x+w] #เป็นการตัดรูปที่อยู่ในกรอบ
        cv2.namedWindow("License Detected : ", cv2.WINDOW_NORMAL)
        cv2.imshow("License Detected : ",license_img) #โชว์รูปที่ถูกตัด
        cv2.drawContours(img, [contour],-1,(0,255,255),3) #การวาด contour 
        gg=pytesseract.image_to_string(license_img, lang='tha+eng')
        print(gg)

cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cv2.imshow("Image",img) #โชว์รูป
cv2.waitKey(0)