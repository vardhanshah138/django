from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import BlogForm
from .models import Blog

def homepage(request):
    return render(request,'blogs/homepage.html')

def blogging(request):
    return render(request,'blogs/blogging.html')

def getimg(request):

    if request.method == 'POST':
        form = BlogForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            print(form)

            return redirect('success/')
    else:
        form = BlogForm()

    context = {'form':form}
    
    return render(request,'blogs/index.html',context)

def success(request):
    return render(request,'blogs/success.html',)
        


def display_media(request):
    medias = Blog.objects.all()
    return render (request,'blogs/showmedia.html',{'img' : medias})
# Create your views here.
