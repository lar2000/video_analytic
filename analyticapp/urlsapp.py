
from django.urls import path
from analyticapp.views import cap_video

urlpatterns = [
    
    path('',cap_video.index),   
]