from django import forms

from .models import CV
class CVForm(forms.ModelForm):
    class Meta:
        model = CV
        fields = ('email',)
        labels = {
            'email' : 'e-mail'
        }