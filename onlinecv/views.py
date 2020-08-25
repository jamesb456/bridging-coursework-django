from django.shortcuts import render

# Create your views here.
def cv_view(request):
    return render(request,"cv.html")

def edit_cv_view(request):
    return render(request,"edit_cv.html")