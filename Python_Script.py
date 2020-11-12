'''
This program scrapes LinkedIn leads & saves them to a CSV file for further follow up by Sales teams
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
    '''Navigates to the homepage of LinkedIn.com. Optional Parameters: Email, Password.'''
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
    '''Finds the search bar on the main page and searches any subject provided by the caller. Default is chatbot'''
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
    '''Takes you from the main search results into the people's tab'''
    time.sleep(3)
    people_tab = driver.find_element_by_xpath('''//li[@class="search-vertical-filter__filter-item mr2"]''')
    time.sleep(2)
    people_tab.click()
    time.sleep(3)
### Navigating to the people tab to find people in the industry

### Start Scraping The Profiles
#print(driver.current_url) gets the current URL of the page that you are on
#print(driver.page_source) gets all the HTML from the current page
def scrape_profile(pages=10):
    '''Default parameter is 10 pages of scraping, can pass any number < 100'''
    ### outer For/While loop contingent on which page I am on, each iteration of loop does the following chunk of code###
    page_iterator = 1
    while page_iterator < pages:
        
        #put the current HTML page in a beautiful soup object
        source = driver.page_source
        soup = BeautifulSoup(source,"lxml")
        
        #finding the name, title and links for a profile
        profiles = defaultdict(list)
        
        for name in soup.find_all(class_=re.compile("name actor-name")):
            for occupation in soup.find_all(class_=re.compile("subline-level-1 t-14 t-black t-normal search-result__truncate")):
                is_parent = [item for item in occupation.parent.stripped_strings]
                if is_parent[0] == name.contents[0]:
                    success = [''.join(occ) for occ in occupation.stripped_strings]
                    for description in soup.find_all(href=re.compile("/in/")): 
                        profiles[(name.contents[0])].append(success[0])
                        profiles[(name.contents[0])].append(("https://www.linkedin.com" + description.attrs['href']))
                        break

        print(profiles.keys())
        print(profiles.values())                
        #Finding the name, title and links for a profile
    
        for title in soup.find_all(class_=re.compile("subline-level-1 t-14 t-black t-normal search-result__truncate")):
            print(title.parent.text)
     

        for profile in soup.find_all(class_=re.compile("search-result search-result__occluded-item ember-view")):
            formatting = profile.text.replace("\n","")
            print(formatting)
            formatting2 = (formatting.strip()).split()
            del formatting2[2]
            key = formatting2[0] + " " + formatting2[1]
            value = ""
            for words in range(len(formatting2)):
                if words > 1:
                    value = " ".join((value, formatting2[words]))
            value = value.strip()
            print(key)
            print(value)

        #for link in soup.find_all(href=re.compile("/in/")):
    

        profile0 = soup.find(class_="search-results-container")
        print(profile0)
        profile1 = profile0.find(class_="search-result__wrapper")
        print(profile1)
        profile2 = profile0.find("span",class_="name actor-name")
        print(profile2)
        profile3 = profile0.find("p",class_="subline-level-1 t-14 t-black t-normal search-result__truncate")
        print(profile3)
        #adding the links for the page to a list
        profile_links = []
        for link in soup.find_all(href=re.compile("/in/")):
            print(link)
            profile_links.append(link.get("href"))
        #choosing the first profile link for the first person    
        profile4 = profile_links[0]
        print("This is a list of the profile links: ", profile_links)
        print()
        #grabbing only the text from the html and stripping out any whitespace
        name = profile2.text
        summary = profile3.text.strip() 
        link = "https://www.linkedin.com" + profile4 
        output = write_csv(name,summary,link)
        #printing to the console the first persons profile information
        print("Name: ",name)
        print()
        print("Title/Summary: ",summary)
        print()
        print("Link: ",link)
        page_iterator += 1
        nextpage = next_page(page_iterator)
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
def write_csv(name,summary,link):
    csv_file = open("lead_gen.csv","a")
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Date","Name","Summary/Title","Link"])
    today = date.today()
    todays_date = today.strftime("%d/%m/%y")
    csv_writer.writerow([todays_date,name,summary,link])
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