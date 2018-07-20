# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
#from .tasks import *
# Create your views here.
import time
import os

def index(request):
    name = request.GET.get('name','logo.jpg')
    name = "uploads/" + name
    #b1task(name)
    return render(request,'api/index.html',context={'imgfile':name})

# TODO:重复文件处理;异常处理，文件损坏则删除;
def upload(request):
    if request.method=="POST":
        myFile =request.FILES.get("file", None)    # 获取上传的文件，如果没有文件，则默认为None
        if not myFile:
            return HttpResponse("no files for upload!")
        handle_upload_file(request)
        #return HttpResponse('woking to upload...') #此处简单返回一个成功的消息，在实际应用中可以返回到指定的页面中
        return HttpResponse('OK') #此处简单返回一个成功的消息，在实际应用中可以返回到指定的页面中
    return render_to_response('api/index.html')

def handle_upload_file(request):
    st = time.time()
    print("start...")
    upfile = request.FILES.get('file')
    filename = upfile.name
    path='api/static/uploads/'     #上传文件的保存路径，可以自己指定任意的路径
    if not os.path.exists(path):
        os.makedirs(path)
    print("I am here upload starting!")
    with open(path+filename,'wb+') as destination:
        for chunk in upfile.chunks():
            destination.write(chunk)
    endt = time.time()
    print("uploadfile {} cost {:.2f}.".format(filename,endt-st))
