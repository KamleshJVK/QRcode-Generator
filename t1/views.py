from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Destination
from django.contrib import messages
from django.shortcuts import render
from django.conf import settings
import os
import uuid

import qrcode

def home(request):
    return render(request,'home.html')

"""def add_url(request):
    if request.method == 'POST':
        name = request.POST.get('url')
        Destination.objects.create(name=name)
    return render(request,'success.html')"""
    

def makeCode(url):
    image = qrcode.make(url)
    
    unique_name =f"{uuid.uuid4()}.jpg"
    path = os.path.join(settings.BASE_DIR,'t1', 'static','img')
    os.makedirs(path, exist_ok=True)
    image.save(os.path.join(path, unique_name))
    return os.path.join('img',unique_name)
    
        
def get_code(request):
    if request.method =='POST':
        name = request.POST.get('url')
        img1=makeCode(name)
        Destination.objects.create(name=name,img=img1)
        return render(request,'image.html', {'img':img1})
    else:
        return render(request,'home.html') 
    
        
    


    
