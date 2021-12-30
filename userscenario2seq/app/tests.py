# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# from django.test import TestCase
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# options.setCapability(CapabilityType.ACCEPT_INSECURE_CERTS, true);
# options.setCapability(CapabilityType.ACCEPT_SSL_CERTS, true);

# Create your tests here.
class LoginFormTest(LiveServerTestCase):
    def testWithWrongPassword(self): #test yang salah
        driver = webdriver.Chrome("D:/PUNYA ICIL/chromedriver.exe")
        selenium = driver
        #Choose your url to visit
        selenium.get('http://127.0.0.1:8000/')
        user_username = selenium.find_element_by_id('id_username')
        user_password = selenium.find_element_by_id('id_password')

        submit = selenium.find_element_by_id('submit_button')

        #populate the form with data
        user_username.send_keys('testing1')
        user_password.send_keys('password salah')

        #submit form
        # submit.send_keys(Keys.RETURN)
        submit.click()

        #check result; page source looks at entire html document
        assert 'Sign IN' in selenium.page_source
    
    def testWithInvalidCredentials(self): #test yang salah
        driver = webdriver.Chrome("D:/PUNYA ICIL/chromedriver.exe")
        selenium = driver
        #Choose your url to visit
        selenium.get('http://127.0.0.1:8000/')
        user_username = selenium.find_element_by_id('id_username')
        user_password = selenium.find_element_by_id('id_password')

        submit = selenium.find_element_by_id('submit_button')

        #populate the form with data
        user_username.send_keys('username salah')
        user_password.send_keys('password salah')

        #submit form
        # submit.send_keys(Keys.RETURN)
        submit.click()

        #check result; page source looks at entire html document
        assert 'Sign IN' in selenium.page_source
    
    def testWithWrongUsername(self): #test yang salah
        driver = webdriver.Chrome("D:/PUNYA ICIL/chromedriver.exe")
        selenium = driver
        #Choose your url to visit
        selenium.get('http://127.0.0.1:8000/')
        user_username = selenium.find_element_by_id('id_username')
        user_password = selenium.find_element_by_id('id_password')

        submit = selenium.find_element_by_id('submit_button')

        #populate the form with data
        user_username.send_keys('username salah')
        user_password.send_keys('passwordtesting')

        #submit form
        # submit.send_keys(Keys.RETURN)
        submit.click()

        #check result; page source looks at entire html document
        assert 'Sign IN' in selenium.page_source
    
    def testWithValidCredentials(self): #test yang betul
        driver = webdriver.Chrome("D:/PUNYA ICIL/chromedriver.exe")
        selenium = driver
        #Choose your url to visit
        selenium.get('http://127.0.0.1:8000/')
        user_username = selenium.find_element_by_id('id_username')
        user_password = selenium.find_element_by_id('id_password')

        submit = selenium.find_element_by_id('submit_button')

        #populate the form with data
        user_username.send_keys('testing1')
        user_password.send_keys('passwordtesting1')

        #submit form
        # submit.send_keys(Keys.RETURN)
        submit.click()

        #check result; page source looks at entire html document
        assert 'Tutorial' in selenium.page_source


# Create your tests here.
