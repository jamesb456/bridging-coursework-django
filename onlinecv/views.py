from django.shortcuts import render
from .forms import CVForm, QualFormSet
from .models import CV, Qualification
# Create your views here.
def cv_view(request):
    return render(request,"onlinecv/cv.html")

def edit_cv_view(request):
    #TODO: TEMP CHANGE PLEASE get cv from database
    cv = CV()
    form = CVForm(instance=cv)

    formset = QualFormSet(instance=cv)
    return render(request,"onlinecv/edit_cv.html",{'form' : form,'formset' : formset})