from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from pyvirtualdisplay import Display
from time import sleep

# Creates a Chrome browser instance and opens Login page
browser = webdriver.Chrome('/Users/Nieceyyyy/Downloads/chromedriver')
browser.get('https://www.coastal.edu/scs/employee')

# Finding input elements for username and password
uname = browser.find_element_by_id('uname')
pword = browser.find_element_by_id('pnum')

# Getting username and password from user input
username = input("What is your username? ")
password = input("What is your password? ")

# Sending keys to elements
uname.send_keys(username)
pword.send_keys(password)

# Submitting filled form
browser.find_element_by_xpath("//input[@type='submit' and @value='Submit']").click()


# Finds hours between pay periods through date picker using from and to dates
from_date = browser.find_element_by_id('from')
ActionChains(browser).move_to_element(from_date).click().send_keys('2017-07-20').perform()
to_date = browser.find_element_by_id('to')
ActionChains(browser).move_to_element(to_date).click().send_keys('2017-07-30').perform()
submit_btn = browser.find_element_by_id('Submit')
ActionChains(browser).move_to_element(submit_btn).click().click().perform()

# Getting JavaScript generated html
sleep(10)
time_card = browser.execute_script("return document.getElementById('reportContent')")

time_info = dict()

# Loops through time_card and serializes information into dictionary containing relevant information
for text in time_card.text.splitlines()[1:-1]:


    line = text.split()
    firstName = line[0]
    lastName = line[1]
    specDate = line[2]
    timeIn = line[3]
    timeOut = line[5]
    location = line[6] + " " + line[7]
    hours = line[8]

    try:
        time_info[specDate].append({
        'Name': firstName + " " + lastName,
        'Time-In': timeIn,
        'Time-Out': timeOut,
        'Location': location,
        'Hours': hours
    })
    except KeyError:
        time_info[specDate] = [{
        'Name': firstName + " " + lastName,
        'Time-In': timeIn,
        'Time-Out': timeOut,
        'Location': location,
        'Hours': hours
    }]


