from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

import time
driver = webdriver.Chrome()


urls = ['https://www.trulia.com/', 'https://www.redfin.com/', 'https://www.compass.com/', 'https://www.realtor.com/', 'https://www.houzeo.com/flat-fee-mls/',
        'https://vanguardproperties.com/']


#refin, compass, houszero, vanguard   works rest of other sites detect bots. 

driver = webdriver.Chrome()

def load_website(url, times):

    for i in range(0, times):
        try:
            driver.get(url)
            time.sleep(1)
        except Exception as error:
            print(error)



for url in urls:
    load_website(url, 6)

driver.quit()



