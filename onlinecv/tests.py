from django.test import TestCase
from django.contrib.auth.models import User
from .forms import CVForm
# Create your tests here.
class CVTest(TestCase):
    
    def setUp(self):
        self.admin_user = User.objects.create(username='james')
        self.admin_user.set_password('jam')
        self.admin_user.save()
        

    def test_uses_cv_template(self):
        response = self.client.get('/cv/')
        self.assertTemplateUsed(response,"onlinecv/cv.html")

    def test_uses_edit_cv_template(self):
        # Its a surpise tool that will help us later
        #self.client.login(username='james',password='jam')
        response = self.client.get('/cv/edit/')
        
        self.assertTemplateUsed(response,"onlinecv/edit_cv.html")

    def test_form_accepts_email(self):
        form = CVForm(data={'email':'stevejobs@apple.com'})
        self.assertTrue(form.is_valid())
    
    def test_form_invalid_email(self):
        form = CVForm(data={'email':''})
        self.assertFalse(form.is_valid())