
from django.urls import path
from analyticapp.views import readnumder_analy, site

urlpatterns = [
    
    path('',site.index),    
]