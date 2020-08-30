from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException

from selenium import webdriver

from django.test import LiveServerTestCase
from django.contrib.auth.models import User

from onlinecv.models import CV, Employment, Skill, Interest, Qualification
from datetime import date

import unittest
import time


MAX_WAIT = 10 

class NewVisitorTest(LiveServerTestCase):  

    def setUp(self):  
        #you might need to change the next 2 lines to get tests to run
        #basically selenium refused to find the firefox executable,
        #so i had to manually point it to it
        self.binary = FirefoxBinary('/usr/lib/firefox/firefox')
        self.browser = webdriver.Firefox(firefox_binary=self.binary)
        self.admin_user = User.objects.create_superuser(username='jamesb',password='jam',email="stevejobs@apple.com")
        self.admin_user.save()
        
    def tearDown(self):  
        self.browser.quit()


    def get_form_element_from_label(self, form, label):
        input_label = form.find_element_by_xpath(f'//label[text()=\'{label}\']')
        element_id = input_label.get_attribute("for")
        element = form.find_element_by_id(str(element_id))
        return element

    def create_valid_cv(self):
        cv = CV.objects.create(author=self.admin_user,email="stevejobs@apple.com",github_profile="https://github.com/jamesb456",personal_statement="Hello. ",linkedin_profile="https://www.linkedin.com/in/james-bray-9548a7172")
        cv.save(commit=False)
        qual = Qualification.objects.create(linked_cv=cv,title="A qualification",start_date=date(2017,3,6),end_date=(2017,4,7),description="A qualification description")
        emp = Employment.objects.create(linked_cv=cv,job_title="A job",start_date=date(2018,3,6),end_date=(2018,7,29),description="A job description")
        sk = Skill.objects.create(linked_cv=cv,description="A skill")
        sk2 = Skill.objects.create(linked_cv=cv,description="Another skill")
        interest = Interest.objects.create(linked_cv=cv,description="A project or interest")
        interest2 = Interest.objects.create(linked_cv=cv,description="Another project or interest")
        qual.save()
        emp.save()
        sk.save()
        sk2.save()
        interest.save()
        interest2.save()
        cv.save()


    def create_valid_cv_empty(self):
        cv = CV.objects.create(author=self.admin_user,email="stevejobs@apple.com",github_profile="https://github.com/jamesb456",personal_statement="Hello. ",linkedin_profile="https://www.linkedin.com/in/james-bray-9548a7172")
        cv.save()

    def test_can_edit_cv(self):
        #assume an existing cv already exists
        self.create_valid_cv_empty()
        #testing editing cv so we need to be logged in
        self.client.login(username='jamesb', password='jam') 
        #this bit needed for login to work correctly
        #so selenium actualy thinks we are logged in
        cookie = self.client.cookies['sessionid']
        self.browser.get(self.live_server_url + '/admin/') 
        self.browser.add_cookie({'name': 'sessionid', 'value': cookie.value, 'secure': False, 'path': '/'})
        self.browser.refresh() 
        self.browser.get(self.live_server_url + '/admin/')

        # James would like to edit his own CV. He first navigates to the web page for it on his web browser
        self.browser.get(self.live_server_url + '/cv/')

        time.sleep(5)
        # The page's title is 'CV'
        self.assertEqual('CV',self.browser.title,f"Expected page title {'CV'}, got {self.browser.title}.")

        # In the header he sees a link to edit his CV. He clicks on it
        link = self.browser.find_element_by_xpath('//header[@id=\'header\']/a[@id=\'btn-edit-cv\']')
        self.assertEqual('Edit CV',link.text,f"Expected text {'Edit CV'}, got {link.text}")
        
        

        link.click()

        # He is taken to a page titled 'Edit CV'
        
        self.assertEqual('Edit CV',self.browser.title,f"Expected title of page to be {'Edit CV'}, got {self.browser.title} instead.")

        # He sees a form which allows him to change the information on his CV
        form = self.browser.find_element_by_xpath('//form[@id=\'form_edit_cv\']')

        
        # Firstly, James needs to edit his e-mail address. He finds a text box with the label
        # 'e-mail:' and replaces the text with 'jxb1123@student.bham.ac.uk'
        
        txt_box_email = self.get_form_element_from_label(form,'e-mail:')
        txt_box_email.send_keys(Keys.CONTROL + "a")
        txt_box_email.send_keys(Keys.DELETE)
        txt_box_email.send_keys("jxb1123@student.bham.ac.uk")

    

        # He now needs to add his github profile. 
        # He finds a text box with the label "Github Profile:"
        # and replaces the text with 'https://github.com/jamesb456'
        txt_box_github = self.get_form_element_from_label(form, 'Github Profile:')
        txt_box_github.send_keys(Keys.CONTROL + "a")
        txt_box_github.send_keys(Keys.DELETE)
        txt_box_github.send_keys("https://github.com/jamesb456")

        # Finally he needs to update his LinkedIn profile
        # He finds a text box with the label "LinkedIn Profile:"
        # and replaces the text with 'https://www.linkedin.com/in/james-bray-9548a7172'
        txt_box_linked = self.get_form_element_from_label(form, 'LinkedIn Profile:')
        txt_box_linked.send_keys(Keys.CONTROL + "a")
        txt_box_linked.send_keys(Keys.DELETE)
        txt_box_linked.send_keys("https://www.linkedin.com/in/james-bray-9548a7172")

        # James then wants to edit his personal statement by adding a sentence.
        # He finds a text area with the label 'Personal Profile:' 
        # and adds a sentence about his passion for test driven development
        
        txt_area_ps = self.get_form_element_from_label(form,'Personal Profile:')
        txt_area_ps.send_keys("My passion for test driven development is unparalled.")

        # Next, James looks at a section of the page entitled 'Education'.
        header_education = form.find_element_by_xpath('//h2[@id=\'header_education\']')
        self.assertEqual("Education",header_education.text,f"Expected header text {'Education'}, got {header_education.text} instead.")
        # He finds a table of qualifications
        qual_table = form.find_element_by_xpath('//table[@id=\'table_qualifications\']')
        # The table is currently empty. However there is a header showing the four things
        # that James will need to input when he adds a qualification:
        # 'Title' , 'Start date', 'End date' and 'Description' (in that order)
        header_fields = qual_table.find_elements_by_xpath('thead/tr/th/label')
        

        self.assertIn("Title",header_fields[0].text)
        self.assertIn("Start date",header_fields[1].text)
        self.assertIn("End date",header_fields[2].text)
        self.assertIn("Description",header_fields[3].text)
        # He realises he needs to add a qualification to reflect his
        # mastery of TDD. Therefore:
        
        # He first presses the button 'Add another qualification'
        add_qualifaction_button = form.find_element_by_xpath('//button[@id=\'add_qualification\']')
        self.assertEqual("Add another qualification",add_qualifaction_button.text,f"Expected button text {'Add qualification'}, got {add_qualifaction_button.text} instead.")
        add_qualifaction_button.click()
        
        # The table now has an additional row, with a text input area for each column of the table
        # In the text box for the column 'Title' James writes 'MSci Testing, Driving and Developing'

        qual_tbody = qual_table.find_element_by_tag_name("tbody")
        qual_first_row = qual_tbody.find_element_by_tag_name("tr")
        qual_cells = qual_first_row.find_elements_by_tag_name("td")
        
        txt_title = qual_cells[0].find_element_by_tag_name("input")
        txt_title.send_keys("MSci Testing, Driving and Developing")

        # In the text box for the column 'Start Date' James replaces the default with '16/05/2020'
        txt_sd =  qual_cells[1].find_element_by_tag_name("input")
        txt_sd.send_keys(Keys.CONTROL + "a")
        txt_sd.send_keys(Keys.DELETE)
        txt_sd.send_keys("16/05/2020")

        # In the text box for the column 'End Date' James replaces the default with '22/08/2020'
        txt_ed = qual_cells[2].find_element_by_tag_name("input")
        txt_ed.send_keys(Keys.CONTROL + "a")
        txt_ed.send_keys(Keys.DELETE)
        txt_ed.send_keys("22/08/2020")

        # The 'Description' column has a larger text box. In it James writes 'something about goats'
        txt_desc = qual_cells[3].find_element_by_tag_name("textarea")
        txt_desc.send_keys("something about goats")

       
        # Now that he has added a qualification, he looks further down the page, finding a section called
        # 'Technical Skills'
        header_technical = form.find_element_by_xpath("//h2[@id=\'header_technical\']")

        self.assertEqual("Technical skills",header_technical.text)
        # James wants to add three skills: Testing, Driving, and Developing

        # There is a button with the text 'Add another skill'
        # James presses this button three times. After this happened
        btn_add_skill = form.find_element_by_xpath("//button[@id=\'add_skill\']")
        self.assertEqual("Add another skill",btn_add_skill.text)

        btn_add_skill.click()
        btn_add_skill.click()
        btn_add_skill.click()


        # he notices that three text boxes have appeared. Each is labeled with the text 'Skill 1' , 'Skill 2'... depending on whether its the
        # first second or third skill.

        txt_skill_1 = self.get_form_element_from_label(form,"Skill 1:")
        txt_skill_2 = self.get_form_element_from_label(form,"Skill 2:")
        txt_skill_3 = self.get_form_element_from_label(form,"Skill 3:")
        
        # In the first box James types 'Testing'
        txt_skill_1.send_keys("Testing")
        # In the second box James types 'Driving'
        txt_skill_2.send_keys("Driving")
        # In the third box James types 'Developing'
        txt_skill_3.send_keys("Developing")

      
        # Further down from this is another section called 'Employment'
        header_employment = form.find_element_by_xpath("//h2[@id=\'header_employment\']")
        self.assertEqual("Employment",header_employment.text)
        # Like the 'Qualifications' section, this contains an empty table. The headers
        # on this table are "Job title" , "Start date" , "End date" and "Description"
        emp_table = form.find_element_by_xpath('//table[@id=\'table_employment\']')
        emp_header_fields = emp_table.find_elements_by_xpath('thead/tr/th/label')
        
        self.assertIn("Job title",emp_header_fields[0].text)
        self.assertIn("Start date",emp_header_fields[1].text)
        self.assertIn("End date",emp_header_fields[2].text)
        self.assertIn("Description",emp_header_fields[3].text)
        # James needs to add some new employment, so he presses the button with the text 'Add new employment'
        add_employment_button = form.find_element_by_xpath('//button[@id=\'add_employment\']')
        self.assertEqual("Add new employment",add_employment_button.text,f"Expected button text {'Add new employment'}, got {add_employment_button.text} instead.")
        add_employment_button.click()

        # The table now has an additional column, with a text input area for each column of the table
        emp_tbody = emp_table.find_element_by_tag_name("tbody")
        emp_first_row = emp_tbody.find_element_by_tag_name("tr")
        emp_cells = emp_first_row.find_elements_by_tag_name("td")

        # In the text box for the column 'Job title' James writes 'Software Development (the testing company)'
        emp_txt_title = emp_cells[0].find_element_by_tag_name("input")
        emp_txt_title.send_keys("Software Development (the testing company)")

       # In the text box for the column 'Start date' James replaces the default with '01/08/2020'
        emp_txt_sd =  emp_cells[1].find_element_by_tag_name("input")
        emp_txt_sd.send_keys(Keys.CONTROL + "a")
        emp_txt_sd.send_keys(Keys.DELETE)
        emp_txt_sd.send_keys("01/08/2020")

        # In the text box for the column 'End date' James replaces the default with '31/08/2020'
        emp_txt_ed = emp_cells[2].find_element_by_tag_name("input")
        emp_txt_ed.send_keys(Keys.CONTROL + "a")
        emp_txt_ed.send_keys(Keys.DELETE)
        emp_txt_ed.send_keys("31/08/2020")

        # The 'Description' column has a larger text box. In it James writes 'I was lucky enough to spend a month at this job.'
        emp_txt_desc = emp_cells[3].find_element_by_tag_name("textarea")
        emp_txt_desc.send_keys("I was lucky enough to spend a month at this job.")  

        
        # There is a final section at the bottom called 'Projects and Interests'
        header_projects_interests = form.find_element_by_xpath("//h2[@id=\'header_projects_interests\']")
        self.assertEqual("Projects/Interests",header_projects_interests.text)
        # James presses the button labeled 'Add another interest/project'
        btn_add_interest = form.find_element_by_xpath("//button[@id=\'add_interest\']")
        self.assertEqual("Add another interest/project",btn_add_interest.text)
        btn_add_interest.click()
        # In the text box that appears he types 'The biology of goats'
        txt_interest = self.get_form_element_from_label(form,"Project/Interest 1:")
        txt_interest.send_keys("The biology of goats")
        # Finally James presses the 'Save' button. Upon the page being reloaded, he sees that the data
        # he entered is preserved    
        btn_save = form.find_element_by_xpath("//button[@id=\'save_form\']")
        btn_save.click()
        

    #new functional test to check that the CV can be created when none exists
    def test_can_create_new_cv(self):
        #James wants to create his CV, but has not done so yet
        
        #He visits the web page         
        self.browser.get(self.live_server_url + "/cv/")

        #The website contains a message conveying that the cv could not be found
        error_heading = self.browser.find_element_by_tag_name("h1")
        self.assertIn("CV not found",error_heading.text)
        # However James sees a button that would allow him to create the CV he needs to.
        create_cv = self.browser.find_element_by_id("btn-create-cv")
        self.assertEqual('Create CV',create_cv.text,f"Expected text {'Create CV'}, got {create_cv.text}")
        create_cv.click()
        # He clicks the button and lands on a page titled 'Edit CV'
        self.assertEqual(self.browser.title,"Edit CV",f"Expected text {'Edit CV'}, got {self.browser.title}")
        # Satisfied, he stops here

        
        
    
    def test_user_facing(self):
        # helper method to create a valid cv to test
        self.create_valid_cv()
        # Edith want's to view someone's CV. She goes to their
        # website to find a link to it
        self.browser.get(self.live_server_url + "/cv/")

        # The page has a link to a CV in the header,
        # which she clicks on.
        self.fail("Finish this test!")
        # She finds that she is immediately presented with
        # their name, picture and contact details i.e
        # * Github profile
        # * LinkedIn Profile
        # * e-mail

        # Further down the page she sees a section of the page titled 
        # 'Personal Profile'

        # This section contains a short paragraph of text describing the person

        # Below this section she sees another titled 'Education'

        # This section contains a series of subsections, each with a:
        # * Title
        # * Date the qualification was taken during
        # * Description

        # Below this section is one titled 'Technical skills'

        # This section contains a bullet pointed list of text

        # Below this section is one titled 'Previous Employment'

        # This section contains a series of subsections, each with a:
        # * Job Title
        # * Date the job was/is taken
        # * Description


        # Below this section is one titled 'Projects & Interests'

        # This section contains a bullet pointed list of text

        # Finally as they are a Computer Science student, Edith
        # would like to make sure that the website is in some way
        # secure. She guesses the url for editing the CV, and navigates to it
        # She is satisfied when a page showing the page is forbidden for her to access
        # appears
    

