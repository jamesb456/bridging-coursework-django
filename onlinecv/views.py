from django.shortcuts import render
from .forms import CVForm
# Create your views here.
def cv_view(request):
    return render(request,"onlinecv/cv.html")

def edit_cv_view(request):
    form = CVForm()
    return render(request,"onlinecv/edit_cv.html",{'form' : form})