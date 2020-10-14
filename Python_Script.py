'''
This program scrapes LinkedIn leads & saves them to a CSV file for further follow up by Sales teams
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

#creating a list to store all the information from each individual person
people = []

### This could be a login function
driver = webdriver.Chrome(PATH)

driver.get('https://www.linkedin.com')

link = driver.find_element_by_link_text('Sign in')
link.click()

search = driver.find_element_by_name('session_key')

time.sleep(2)

search.send_keys('sour.monkey.is.great@gmail.com')
    
search2 = driver.find_element_by_name('session_password')

time.sleep(2)

search2.send_keys('Sourmonkey1996')


link2 = driver.find_element_by_class_name('login__form_action_container')
link2.click()

time.sleep(4)
### This could be a login fucntion

### Navigating to search bar and searching an industry

link3 = driver.find_element_by_xpath('''//div[@id="global-nav-search"]''')

time.sleep(2)

link3.click()

link4 = driver.find_element_by_xpath('''//input[@class="search-global-typeahead__input always-show-placeholder"]''')

time.sleep(3)

link4.send_keys("chatbot")

time.sleep(1)

link4.send_keys(Keys.RETURN)

### Navigating to search bar and searching an industry

### Navigating to the people tab to find people in the industry

time.sleep(3)

link5 = driver.find_element_by_xpath('''//li[@class="search-vertical-filter__filter-item mr2"]''')

time.sleep(2)

link5.click()

### Navigating to the people tab to find people in the industry

### Start Scraping The Profiles

time.sleep(3)

source = driver.page_source

soup = BeautifulSoup(source,"lxml")

profile = soup.find(class_="search-result__wrapper")
profile2 = profile.find("span",class_="name actor-name")
profile3 = profile.find("p",class_="subline-level-1 t-14 t-black t-normal search-result__truncate")
print(profile)
print(profile2)
print(profile3)

#print(driver.current_url) gets the current URL of the page that you are on
#print(driver.page_source) gets all the HTML from the current page

test1 = profile2.text
test2 = profile3.text 

print(test1,test2)
### Start Scraping the Profiles

###