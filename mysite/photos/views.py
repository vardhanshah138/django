from django.shortcuts import render,redirect
from .forms import photoForm
from django.http import HttpResponse
import os

# Create your views here.

def upload_record(request):

    if request.method == 'POST':
        form = photoForm(request.POST,request.FILES)            #all the data passed via request.POST stored in request.FILES if only passed through encoded format.

        if form.is_valid():
            form.save()
            filename_img = form.cleaned_data['image_upload']
            filename_vid = form.cleaned_data['video_upload']
            print(filename_vid)
            return render(request,'photos/success.html',{"filename_img" : filename_img,"filename_vid" : filename_vid})                       
    else:
        form = photoForm()
    
    return render(request,'photos/upload.html',{'form':form})                       

def success(request):
    return HttpResponse('successfully uploaded')