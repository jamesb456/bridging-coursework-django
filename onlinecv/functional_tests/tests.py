from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException

from selenium import webdriver

from django.test import LiveServerTestCase
from django.contrib.auth.models import User

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
        self.admin_user = User.objects.create(username='james')
        self.admin_user.set_password('jam')
        self.admin_user.save()

    def tearDown(self):  
        self.browser.quit()


    def get_form_element_from_label(self, form, label):
        input_label = form.find_element_by_xpath(f'//label[text()=\'{label}\']')
        element_id = input_label.get_attribute("for")
        element = form.find_element_by_id(str(element_id))
        return element

    def test_can_edit_cv(self):
        
        #self.client.login(username='james',password='jam')
        # James would like to edit his own CV. He first navigates to the web page for it on his web browser
        self.browser.get(self.live_server_url + '/cv/')

        
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
        header_fields = qual_table.find_elements_by_xpath('//thead/tr/th/label')
        

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
        header_technical = form.find_element_by_xpath("//h2[@id=\'header_employment\']")
        self.assertEqual("Employment",header_technical.text)
        # Like the 'Qualifications' section, this contains an empty table. The headers
        # on this table are "Job Title" , "Start Date" , "End date" and "Description"
        emp_table = form.find_element_by_xpath('//table[@id=\'table_employment\']')
        emp_header_fields = emp_table.find_elements_by_xpath('//thead/tr/th/label')
        
        self.assertIn("Job Title",emp_header_fields[0].text)
        self.assertIn("Start date",emp_header_fields[1].text)
        self.assertIn("End date",emp_header_fields[2].text)
        self.assertIn("Description",emp_header_fields[3].text)
        # James needs to add some new employment, so he presses the button with the text 'Add New Employment'
        add_employment_button = form.find_element_by_xpath('//button[@id=\'add_employment\']')
        self.assertEqual("Add New Employment",add_qualifaction_button.text,f"Expected button text {'Add New Employment'}, got {add_employment_button.text} instead.")
        add_employment_button.click()

        # The table now has an additional column, with a text input area for each column of the table
        emp_tbody = emp_table.find_element_by_tag_name("tbody")
        emp_first_row = emp_tbody.find_element_by_tag_name("tr")
        emp_cells = emp_first_row.find_elements_by_tag_name("td")

        # In the text box for the column 'Title' James writes 'Software Development (the testing company)'
        emp_txt_title = emp_cells[0].find_element_by_tag_name("input")
        emp_txt_title.send_keys("MSci Testing, Driving and Developing")

       # In the text box for the column 'Start Date' James replaces the default with '01/08/2020'
        emp_txt_sd =  emp_cells[1].find_element_by_tag_name("input")
        emp_txt_sd.send_keys(Keys.CONTROL + "a")
        emp_txt_sd.send_keys(Keys.DELETE)
        emp_txt_sd.send_keys("01/08/2020")

        # In the text box for the column 'End Date' James replaces the default with '31/08/2020'
        emp_txt_ed = emp_cells[2].find_element_by_tag_name("input")
        emp_txt_ed.send_keys(Keys.CONTROL + "a")
        emp_txt_ed.send_keys(Keys.DELETE)
        emp_txt_ed.send_keys("31/08/2020")

        # The 'Description' column has a larger text box. In it James writes 'I was lucky enough to spend a month at this job.'
        emp_txt_desc = emp_cells[3].find_element_by_tag_name("textarea")
        emp_txt_desc.send_keys("I was lucky enough to spend a month at this job.")  

        self.fail("Finish the test!")
        # There is a final section at the bottom called 'Projects and Interests'
        # James presses the button labeled 'Add another interest/project'
        # In the text box that appears he types 'The biology of goats'
        
        # Finally James presses the 'Save' button. Upon the page reloaded he sees that the data
        # he entered is preserved    


        


        
        
    
    def test_user_facing(self):
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
    

