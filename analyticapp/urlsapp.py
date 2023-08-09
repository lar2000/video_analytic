
from django.urls import path
from analyticapp.views import img_analytic, site

urlpatterns = [
    
    path('',site.index),    
]