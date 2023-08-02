from django.db import models

# Create your models here.  
class CCTV(models.Model):
    cctv_id = models.CharField(max_length=10)
    video = models.FileField(upload_to='videos_uploaded',null=True)
    images = models.ImageField(null=True, upload_to='upload_img')
    adress = models.CharField(max_length=100)
    datetime = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.adress + ", "+str(self.video) + ", "+str(self.datetime)
    
class data(models.Model):
    plate_number = models.CharField(max_length=10, null=True)
    bland = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    color_plate = models.CharField(max_length=100)
    province = models.CharField(max_length=255)
    
    