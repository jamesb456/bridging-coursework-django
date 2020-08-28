from django import forms

from .models import CV, Qualification
from django.forms import inlineformset_factory
class CVForm(forms.ModelForm):
    class Meta:
        model = CV
        fields = ('email','github_profile','linkedin_profile','personal_statement')
        labels = {
            'email' : 'e-mail',
            'github_profile' : 'Github Profile',
            'linkedin_profile' : 'LinkedIn Profile',
            'personal_statement' : 'Personal Profile'
        }
        




QualFormSet = inlineformset_factory(CV,Qualification,fields=('title','start_date','end_date','description'),labels=('Title','Start Date','End Date','Description'),extra=0,can_delete=False)