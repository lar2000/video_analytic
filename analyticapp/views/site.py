from django.shortcuts import render
from analyticapp.models import Media

# Create your views here.  

def index(request):
    all_data = Media.objects.all()
    return render(request, "cctv.html",{"all_data":all_data})