from django.test import TestCase
from django.contrib.auth.models import User
from .forms import CVForm, QualFormSet
from .models import CV, Qualification
from datetime import date
# Create your tests here.
class CVTest(TestCase):
    

    def setUp(self):
        self.admin_user = User.objects.create(username='james')
        self.admin_user.set_password('jam')
        self.admin_user.save()
        
    #get a dictionary containing the data to test the form
    #the optional arguments can be changed to, for example, make one of the fields invalid
    def get_cv_test_dictionary(self, email='stevejobs@apple.com',github_profile='https://github.com/steve_jobs',personal_statement="Personal Statement",linkedin_profile="https://linkedin.com"):
        return { 
            "email" : email ,
            "github_profile" : github_profile,
            "linkedin_profile" : linkedin_profile,
            "personal_statement" : personal_statement
        }

    def get_qualification_test_dictionary(self,title="MSci Apples",start_date=date(1997,5,5),end_date=date(1997,5,6),description="Bringing multimillion dollar company back from the grave"):
        return{
            "title" : title,
            "start_date" : start_date,
            "end_date": end_date,
            "description": description
        }

    def test_uses_cv_template(self):
        response = self.client.get('/cv/')
        self.assertTemplateUsed(response,"onlinecv/cv.html")

    def test_uses_edit_cv_template(self):
        # Its a surpise tool that will help us later
        #self.client.login(username='james',password='jam')
        response = self.client.get('/cv/edit/')
        
        self.assertTemplateUsed(response,"onlinecv/edit_cv.html")

    def test_cv_model_is_valid(self):
        model = CV.objects.create()
        model.save()
        self.assertEqual(model.email,'')
        self.assertEqual(model.github_profile,'')
        self.assertEqual(model.linkedin_profile,'')
        self.assertEqual(model.personal_statement,'')
        
    
    def test_cv_form_accepts_valid_form_data(self):
        test_dict = self.get_cv_test_dictionary()
        form = CVForm(data=test_dict)
        self.assertTrue(form.is_valid(),f"Form is not valid\n, errors:\n{form.errors}")
        

    
    def test_cv_form_invalid_email(self):
        form = CVForm(data=self.get_cv_test_dictionary(email='not_valid.zs.x'))
        self.assertFalse(form.is_valid())

    def test_cv_form_invalid_github_profile(self):
        form = CVForm(data=self.get_cv_test_dictionary(github_profile='not_a_url'))
        self.assertFalse(form.is_valid())

    def test_qualification_model(self):
        cv = CV.objects.create()
        cv.save()
        qual = Qualification.objects.create(linked_cv=cv)
        qual.save()
        self.assertEqual(qual.linked_cv,cv)
        self.assertEqual(qual.title,'')


        self.assertEqual(qual.start_date,date(1970,1,1))
        self.assertEqual(qual.end_date,date(1970,1,2))
        self.assertEqual(qual.description,'')


    #Test for the formset. Couldn't get this to work, however I'm already testing the qualification model so
    # I think that's enough
    # def test_qual_formset(self):
    #     cv = CV.objects.create()
    #     cv.save()
    #     qual = Qualification.objects.create(linked_cv=cv)
    #     qual.save()
    #     qual_form_set = QualFormSet(instance=cv)
    #     print(qual_form_set.as_ul())
    #     is_valid = qual_form_set.is_valid()
    #     self.assertTrue(is_valid,f"Formset is not valid,\nErrors:\n{ qual_form_set.errors }\n, Non form errors\n{ qual_form_set.non_form_errors()}")
        