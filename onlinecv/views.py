from django.shortcuts import render , get_object_or_404
from django.core.exceptions import PermissionDenied 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import CVForm, QualFormSet, SkillFormSet, EmploymentFormSet, InterestFormSet
from time import sleep
from .models import CV, Qualification
# Create your views here.
def cv_view(request):
    #hardcode to only see my CV (this is bad)
    cv = get_object_or_404(CV,author=User.objects.get(username="jamesb"))
    return render(request,"onlinecv/cv.html" , {'cv' :cv})

# @login_required would use this if I put a login screen
def edit_cv_view(request):
    if(request.user != User.objects.get(username="jamesb")):
        raise PermissionDenied(f"{request.user.name} cannot edit jamesb's CV")

    (cv, created) = CV.objects.get_or_create(author=request.user)
    if(created):
        cv.save()
    
    form = CVForm(instance=cv)
    author = cv.author
    if request.method =="POST":
        form = CVForm(request.POST, instance=cv)
        if(form.is_valid()):
            saved_cv = form.save(commit=False)
            formset_qual = QualFormSet(request.POST,instance=saved_cv)
            formset_skill = SkillFormSet(request.POST,instance=saved_cv)
            formset_emp = EmploymentFormSet(request.POST,instance=saved_cv)
            formset_interest = InterestFormSet(request.POST,instance=saved_cv)
            if(formset_qual.is_valid() and formset_skill.is_valid() and formset_emp.is_valid() and formset_interest.is_valid()):
                saved_cv.save()
                formset_qual.save()
                formset_skill.save()
                formset_emp.save()
                formset_interest.save()
            
                

            return render(request,"onlinecv/edit_cv.html",{
                'form' : form,
                'formset_qual' : formset_qual , 
                'formset_skill' : formset_skill,
                'formset_emp' : formset_emp,
                'formset_interest' :formset_interest,
                'author' : author
            })
    else:
        formset_qual = QualFormSet(instance=cv)
        formset_skill = SkillFormSet(instance=cv)
        formset_emp = EmploymentFormSet(instance=cv)
        formset_interest = InterestFormSet(instance=cv)
        return render(request,"onlinecv/edit_cv.html",{
            'form' : form,
            'formset_qual' : formset_qual , 
            'formset_skill' : formset_skill,
            'formset_emp' : formset_emp,
            'formset_interest' :formset_interest,
            'author' : author
        })


    