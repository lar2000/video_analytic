
from django.urls import path
from analyticapp.views import vdo_analytic, site

urlpatterns = [
    
    path('',site.index),    
]