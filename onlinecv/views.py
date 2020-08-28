from django.shortcuts import render
from .forms import CVForm, QualFormSet, SkillFormSet
from .models import CV, Qualification
# Create your views here.
def cv_view(request):
    return render(request,"onlinecv/cv.html")

def edit_cv_view(request):
    if not request.POST:
        #TODO: TEMP CHANGE PLEASE get cv from database
        cv = CV()
        form = CVForm(instance=cv)

        formset_qual = QualFormSet(instance=cv)
        formset_skill = SkillFormSet(instance=cv)
        
        return render(request,"onlinecv/edit_cv.html",{'form' : form,'formset_qual' : formset_qual , 'formset_skill' : formset_skill})