'''
This program scrapes Linkedin leads & saves them to a CSV file for further follow up by Sales teams.
'''
#importing required libraries & modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import lxml
import time
import csv
import re
from datetime import date
from collections import defaultdict

###setting up the path where I placed the chromedriver executable file### 
PATH = '/Users/warrenwilliams/Desktop/LinkedIn/chromedriver'
driver = webdriver.Chrome(PATH)
###you might have some permission erros with Mac OS, this link should fix it https://docwhat.org/upgrading-to-catalina###



### Login Function
def homepage_login(email='sour.monkey.is.great@gmail.com',password='Sourmonkey1996'):
    '''Navigates to the homepage of Linkedin.com. Optional Parameters: Email, Password.'''
    driver.get('https://www.linkedin.com')
    sign_in_button = driver.find_element_by_link_text('Sign in')
    sign_in_button.click()
    find_email = driver.find_element_by_name('session_key')
    time.sleep(2)
    find_email.send_keys(email)
    find_password = driver.find_element_by_name('session_password')
    time.sleep(2)
    find_password.send_keys(password)
    account_login = driver.find_element_by_class_name('login__form_action_container')
    account_login.click()
    time.sleep(4)
### Login Function

### Navigating to search bar and searching an industry
def search_bar(subject="chatbot"):
    '''Finds the search bar on the main page and searches any subject provided by the caller. Default is chatbot.'''
    find_searchbar = driver.find_element_by_xpath('''//div[@class="global-nav__search "]''')
    time.sleep(2)
    find_searchbar.click()
    enter_searchbar = driver.find_element_by_xpath('''//input[@class="search-global-typeahead__input always-show-placeholder"]''')
    time.sleep(3)
    enter_searchbar.send_keys(subject)
    time.sleep(1)
    enter_searchbar.send_keys(Keys.RETURN)
### Navigating to search bar and searching an industry

### Navigating to the people tab to find people in the industry
def people_tab():
    '''Takes you from the main search results into the people's tab.'''
    time.sleep(3)
    people_tab = driver.find_element_by_xpath('''//li[@class="search-vertical-filter__filter-item mr2"]''')
    time.sleep(2)
    people_tab.click()
    time.sleep(3)
### Navigating to the people tab to find people in the industry

### Start Scraping The Profiles
def scrape_profile(pages=2):
    '''Default parameter is 5 pages of scraping, can pass any number < 100. Recommended to keep low otherwise Linkedin might flag your account.'''
    #all Linkedin profiles are stored in the variable/identifier: profiles
    page_iterator = 0
    profiles = defaultdict(list)
    while page_iterator < pages:
        
        #put the current HTML page in a beautiful soup object
        source = driver.page_source
        soup = BeautifulSoup(source,"lxml")
        
        #finding the name, title and url for a profile
        for name in soup.find_all(class_=re.compile("name actor-name")):
            for title in soup.find_all(class_=re.compile("subline-level-1 t-14 t-black t-normal search-result__truncate")):
                #matching up the name and the title, the Linkedin DOM is INSANE!
                match_up = [item for item in title.parent.stripped_strings]
                if match_up[0] == name.contents[0]:
                    is_match = [''.join(occ) for occ in title.stripped_strings]
                    #finding the correct url/link
                    for url in soup.find_all(href=re.compile("/in/")):
                        link = "https://www.linkedin.com"
                        checker = url.attrs["href"]
                        link += checker
                        if link in [item for items in profiles.values() for item in items]:
                            continue 
                        profiles[(name.contents[0])].append(is_match[0])
                        profiles[(name.contents[0])].append(link)
                        break
                    break

        print(profiles.keys())
        print(profiles.values()) 

        #navigating to the next page
        nextpage = next_page(page_iterator)
        page_iterator += 1

    #writing to the csv
    write_profiles = write_csv(profiles)    
### Start Scraping the Profiles

### Navigating to the next page for scraping 
def next_page(page_number):
    '''Navigates to the next page on the LinkedIn search result. Must pass in next page number as a paramater'''
    pagenumber = page_number
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    pagination = driver.find_element_by_xpath('''//button[@class="artdeco-pagination__button artdeco-pagination__button--next artdeco-button artdeco-button--muted artdeco-button--icon-right artdeco-button--1 artdeco-button--tertiary ember-view"]''')
    time.sleep(2)
    pagination.click()
    time.sleep(3)
### Navigating to the next page for scraping 

### Writing to the CSV File
def write_csv(profiles):
    csv_file = open("lead_gen.csv","a")
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Date","Name","Summary/Title","Link"])
    today = date.today()
    todays_date = today.strftime("%d/%m/%y")
    for item in profiles.items():
        csv_writer.writerow([todays_date,item[0],item[1][0],item[1][1]])
    csv_file.close()
### Writing to the CSV File

def main():
    homepage = homepage_login()
    searchbar = search_bar()
    peopletab = people_tab()
    scrapeprofile = scrape_profile()
    print("SCRAPE COMPLETED")

if __name__ == "__main__":
    main()

### Reading CSV back into memory
'''
def read_scraped_profiles(file_name="lead_gen.csv"):
scraped_profiles = {}
read_file = open(file_name,"r")
csv_contents = csv.reader(read_file)
line_count = 0
for items in csv_contents:
    if line_count != 0:
        scraped_profiles[items[1]] = items[2:4]
    line_count += 1
read_file.close()
'''
### Reading CSV back into memory