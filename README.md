![alt text](https://github.com/williamswarren/Dashbot-Project/blob/master/Thumbnail%20Lead_Generation.png)

# Good To Know:

* Has not been tested on Windows machines.
* Will only work with Google Chrome, hence you will need Google Chrome installed.
* Can be run in demo mode and custom mode. Demo is to see how the script runs and Custom will allow you to run your own custom scrape.
* You might experience issues with the custom scrape. Unfortunately, LinkedIn's UI is not consistent across all its users, meaning my implementation worked for my LinkedIn account, but might not work for yours. If this happens, please use the demo scrape, and give the subject and amount of pages you want to scrape.
* Only scrapes profiles that have names that are within a few degree connections --- meaning no profiles with "LinkedIn Member" as name.
* If your internet connection lags, LinkedIn lags or LinkedIn hits you with a "Please complete this Recaptcha" the script will unfortunately break. Please complete the Recaptcha and you will need to control-c the file. After doing this, re-run the script and it should work.


# Instructions to run the LinkedIn Scraper:

0. Open Terminal.
1. git clone https://github.com/williamswarren/Dashbot-Project.git into whichever directory you would like.
2. Inside the Dashbot-Project you will need to create a virtual environment to install the neccessary dependencies locally.
3. Open Terminal on Mac and cd Dashbot-Project
4. Now type into the terminal, python3 -m venv whatevernameyouwant
5. Activate the virtual environment with, source whatevernameyouwant/bin/activate
6. Now type, pip3 install -r requirements.txt
7. Now you are good to run the file, type into the Terminal, python3 LinkedIn_Script.py
