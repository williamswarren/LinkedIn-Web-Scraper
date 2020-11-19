Good To Know:

Has not been tested on Windows machines.
Will only work with Google Chrome, hence you will need Google Chrome installed.
You might experience issues with the wrong Chromedriver executable, in this case there is comment in the LinkedIn_Script.py file which will direct you to a website for more help.
You MUST BE LOGGED OUT of your account for this to work.
Can be run in demo mode and custom mode. Demo is to see how the executable runs and Custom will allow you to run your own custom scrape.
Only scrapes profiles that have names that are within a few degree connections --- meaning no profiles with "LinkedIn Member" as name.
If your internet connection lags, LinkedIn lags or LinkedIn hits you with a "Please complete this Recaptcha" the script will unfortunately break. Please complete the Recaptcha and you will need to control-c the file. After doing this, re-run the script and it should work.


Instructions to run the LinkedIn Scrapper:

1. git clone https://github.com/williamswarren/Dashbot-Project.git into whichever directory you would like.
2. Inside the Dashbot-Project you will need to create a virtual environment to install the neccessary dependencies locally.
3. Open Terminal on Mac and cd Dashbot-Project
4. Now type into the terminal, python3 -m venv whatevernameyouwant
5. Activate the virtual environment with, source whatevernameyouwant/bin/activate
6. Now type, pip3 install -r requirements.txt
7. Keep the terminal window open in the background. Open the LinkedIn_Script.py file in any IDE.
8. At the top of the file there is a variable/identifier called "PATH". You will need to update the path to the correct pathway for the chromedriver. The chromedriver executable is already downloaded in the Dashbot-Project file, all you need to do is change the PATH to e.g. /Users/yourusername/yourfilepath/Dashbot-Project/chromedriver
9. Now you are good to run the file, bring the Terminal back into view and type, python3 LinkedIn_Script.py
