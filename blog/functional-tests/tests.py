from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException

from selenium import webdriver

from django.test import LiveServerTestCase
import unittest
import time


MAX_WAIT = 10 

class NewVisitorTest(LiveServerTestCase):  

    def setUp(self):  
        self.binary = FirefoxBinary('/usr/lib/firefox/firefox')
        self.browser = webdriver.Firefox(firefox_binary=self.binary)

    def tearDown(self):  
        self.browser.quit()



    
    def test_user_facing(self):
        # Edith want's to view someone's CV. She goes to their
        # website to find a link to it
        self.browser.get(self.live_server_url)

        # The page has a link to a CV in the header,
        # which she clicks on.

        # She finds that she is immediately presented with
        # their name, picture and contact details i.e
        # * Github profile
        # * LinkedIn Profile

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

    

