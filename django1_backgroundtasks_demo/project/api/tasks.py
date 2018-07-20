# -*- coding:utf-8 -*-
import time
import os

from background_task import background

@background(schedule=0)
def b1task(name):
    st = time.time()
    time.sleep(5)
    endt = time.time()
    print("b1task {} cost {:.2f}.".format(name,endt-st)) 

@background(schedule=0)
def handle_upload_file(request):
    st = time.time()
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
