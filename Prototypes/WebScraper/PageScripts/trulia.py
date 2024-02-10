from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

import time
driver = webdriver.Chrome()



#IDEA: Since website detects bot, we can try getting our intended elements, if it detects element won't be present and throw an error and we will know 
#the website detects, otherwise element is found and we know the website doesn't detect atleast in the number of runs we tested. 

#NOTE: Just add the url of site and a element to this array
urls = [('https://www.trulia.com/', By.XPATH, '/html/body/div[1]/div[1]/main/div[1]/div/div/div[2]/div/div[3]/div/div/div/div/div/div/div/div[1]/div/div/input'),
        ('https://www.redfin.com/', By.XPATH, '/html/body/div[1]/div[6]/div[2]/div/section/div/div/div/div/div/div/div/div[2]/div/div/form/div/div/input'), 
        ('https://www.compass.com/', By.XPATH, '/html/body/main/section[1]/div[2]/div/div[2]/div[3]/div/input'), 
        ('https://www.realtor.com/', By.XPATH, '/html/body/div[1]/div/div[1]/div[3]/div[1]/div/div[1]/div[2]/div/div/div/header/div/div/div/input'), 
        ('https://www.houzeo.com/flat-fee-mls/', By.XPATH, '/html/body/section[1]/div/div/div/div[1]/div[1]/div[1]/input'),
        ('https://www.zillow.com/homes/for_rent/', By.XPATH, '/html/body/div[1]/div/div[2]/div/section/div[1]/div/form/div/div/input')
        ]

urls = [
     ('https://www.realtor.com/', By.XPATH, '/html/body/div[1]/div/div[1]/div[3]/div[1]/div/div[1]/div[2]/div/div/div/header/div/div/div/input')
]
working = []


driver = webdriver.Chrome()
def load_website(url, times, element=None):
    global works

    for i in range(0, times):
        try:
            
            driver.get(url)
            if(element != None):
                time.sleep(1)
                searched = driver.find_element(element[0], element[1])
                works = True
            time.sleep(1)
        except Exception as error:
            works = False
            print(error)
        
    if(works == True):
        working.append(url)



for url in urls:
    load_website(url[0], 3, (url[1], url[2]))


print("working urls: ", working)
driver.quit()



