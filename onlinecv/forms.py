from django import forms

from .models import CV
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