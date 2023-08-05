from django.db import models

# Create your models here.  
class Media(models.Model):
    title = models.CharField(max_length=255)
    video = models.FileField(upload_to='assets/video/',null=True)
    images = models.FileField(upload_to='assets/img/',null=True)
    adress = models.CharField(max_length=200)
    datetime = models.DateTimeField()
    
    def __str__(self):
        return self.title
    
    