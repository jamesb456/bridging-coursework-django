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
        self.binary = FirefoxBinary('/usr/lib/firefox/firefox')
        self.browser = webdriver.Firefox(firefox_binary=self.binary)
        self.admin_user = User.objects.create(username='james')
        self.admin_user.set_password('jam')
        self.admin_user.save()

    def tearDown(self):  
        self.browser.quit()


    def test_can_edit_cv(self):
        
        #self.client.login(username='james',password='jam')
        # James would like to edit his own CV. He first navigates to it on his web browser
        self.browser.get(self.live_server_url + '/cv/')

        
        # The page's title is 'CV'
        self.assertEqual('CV',self.browser.title,f"Expected page title {'CV'}, got {self.browser.title}.")

        # In the header he sees a link to edit his CV. He clicks on it
        button = self.browser.find_element_by_xpath('//header[@id=\'header\']/a[@id=\'btn-edit-cv\']')
        self.assertEqual('Edit CV',button.text,f"Expected button text {'Edit CV'}, got {button.text}")
        button.click()
        # He is taken to a page titled 'Edit CV'
        
        self.assertEqual('Edit CV',self.browser.title,f"Expected title of page to be {'Edit CV'}, got {self.browser.title} instead.")

        self.fail("Finish the test")
        # Firstly, James needs to edit his e-mail address. He finds a text box labeled
        # 'e-mail' and replaces the text with 'jxb1123@student.bham.ac.uk'

        # James then wants to edit his personal statement by adding a sentence.
        # He finds a text box labeled 'Personal Statement' and adds a sentence
        # about his passion for Test Driven Development

        # Next, James looks at a section of the page entitled 'Education'.
        # He realises he needs to add an extra qualification to reflect his
        # mastery of TDD. Therefore:
        # He first presses the button 'Add qualification'

        # This reveals four new text boxes and a 'Submit' button

        # In the text box labeled 'Title' James writes 'MSci Testing, Driving and Developing'

        # In the text box labeled 'Start Date' James writes '16/05/2020'

        # In the text box labeled 'End Date' James writes '22/08/2020'
        
        # In the text box labeled 'Description' James writes 'something about goats'

        # He then presses the 'Submit' button. 
        # There is now a table showing the details he just entered




        
        
    
    def test_user_facing(self):
        # Edith want's to view someone's CV. She goes to their
        # website to find a link to it
        self.browser.get(self.live_server_url)

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

    

