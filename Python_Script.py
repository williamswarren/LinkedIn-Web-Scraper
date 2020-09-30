'''
This program scraps LinkedIn leads & saves them to a CSV file for further follow up by Sales teams
'''
#importing required libraries & modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import time

#setting up the path where I placed the chromedriver executable file 
#you might have some permission erros with Mac OS, this link should fix it https://docwhat.org/upgrading-to-catalina
PATH = '/Users/warrenwilliams/Desktop/LinkedIn/chromedriver'

driver = webdriver.Chrome(PATH)

driver.get('https://www.linkedin.com')

link = driver.find_element_by_link_text('Sign in')
link.click()

search = driver.find_element_by_name('session_key')
search.send_keys('sour.monkey.is.great@gmail.com')

search2 = driver.find_element_by_name('session_password')
search2.send_keys('Sourmonkey1996')

link2 = driver.find_element_by_class_name('login__form_action_container')
link2.click()