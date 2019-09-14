#======================================For *MaskRCNN* model=========================================
from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from .forms import *
import cv2,glob,os
from keras_mask_rcnn import maskrcnn_predict
import warnings
warnings.simplefilter("ignore")

global form
form = None

def image_view(request):
    for i in glob.glob("media/images/*"):
        os.remove(i)
    for i in glob.glob("media/output/*"):
        os.remove(i) 
    if request.method == 'POST':
        form = UploadForm()
        form = UploadForm(request.POST, request.FILES) 
        if form.is_valid():
            #print("===> form if <===") 
            form.save() 
            return redirect('success') 
    else:
        #print("===> form else <===")
        form = UploadForm()
        return render(request, 'home_index.html', {'form' : form}) 
    
def success(request):
    im = maskrcnn_predict.predict_results()
    os.remove("media/images/"+im)
    return render(request, 'output_screen.html')
def output_screen(request):
    return render(request,'output_screen.html')
'''
#======================================For *YOLO* model=========================================
from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from .forms import *
import cv2,glob,os
from Yolo_model import yolo
import warnings
warnings.simplefilter("ignore")

global form
form = None

def image_view(request):
    for i in glob.glob("media/images/*"):
        os.remove(i)
    for i in glob.glob("media/output/*"):
        os.remove(i) 
    if request.method == 'POST':
        form = UploadForm()
        form = UploadForm(request.POST, request.FILES) 
        if form.is_valid():
            #print("===> form if <===") 
            form.save() 
            return redirect('success') 
    else:
        #print("===> form else <===")
        form = UploadForm()
        return render(request, 'home_index.html', {'form' : form}) 
    
def success(request):
    #====================================for *YOLO* model===============================
    im = yolo.yolo_model_predict()
    os.remove("media/images/"+im)
    return render(request, 'output_screen.html')
    
def output_screen(request):
    return render(request,'output_screen.html')
'''