from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import requests
import io
from PIL import Image
from collections import deque



class Delay():

    def __init__(self, value):
        self.time = value
    
    def set(self, time):
        self.time = time

    def run(self):
        time.sleep(self.time)



class Bot():

    def __init__(self, url, driver):
        self.url = url
        self.driver = driver
        self.driver.get(self.url)
        self.current_element = None
        self.delayed_search_time = 0.5
        self.delay = Delay(0.5)
        self.stack = deque()

    def search_element(self, by, identifier):
        element = None
        try:
            element = self.driver.find_element(by, identifier)
            self.current_element = element
            self.delay.run()
            return self
        except Exception as error:
            print(".search element() failed!")
            return self
    
    def search_elements(self, by, identifier):
        elements = None
        try:
            elements = self.driver.find_elements(by, identifier)
            self.current_element = elements
            self.delay.run()
            return self
        
        except Exception as error:
            print(".search_elements() failed!")
            return self
    
    def next_page(self, url):
        self.url = url
        self.stack.append(url)
        self.driver.get(self.url)
        return self
    
    def back_page(self):
        self.stack.pop()
        self.url = self.stack[-1]
        self.driver.get(self.url)

    def set_driver(self, driver):
        self.driver = driver
        return self
    
    def wait(self, _time):
        time.sleep(_time)
        return self
    
    def scroll(self, percent):
        return self
    
    def click(self, r1, r2):
        if(isinstance(self.current_element, list) == False):
            self.current_element.click()
        
        elif(isinstance(self.current_element, list) == True):
            try:
                if(r1 == None and r2 == None):
                    for el in self.current_element:
                        el.click()
                else:
                    for i in range(r1, r2+1):
                        self.current_element[i].click()
            except Exception as error:
                print(".click() failed!")
            
            return self
    
    def get_element(self):
        return self.current_element

    def search_delay(self, delay):
        self.delay.set(delay)
        return self




def click_option(bot):
    
    #Click on the selection button for sale/rent
    xpath_main = '/html/body/div[1]/div[8]/div[2]/div[1]/div[2]/div/div/div/div[1]/form/div[1]/div'
    bot.search_element(By.XPATH, xpath_main).get_element().click()

    xpath_radio_rent = '/html/body/div[1]/div[8]/div[2]/div[1]/div[2]/div/div/div/div[1]/form/div[1]/div/div[2]/div/div[1]/div[2]/span/input'
    bot.search_element(By.XPATH, xpath_radio_rent).get_element().click()

    donexpath = '/html/body/div[1]/div[8]/div[2]/div[1]/div[2]/div/div/div/div[1]/form/div[1]/div/div[2]/div/div[2]/button'
    bot.search_element(By.XPATH, donexpath).get_element().click()


def home_type(bot):

    pass

driver = webdriver.Chrome()
url = 'https://www.redfin.com/city/30818/TX/Austin/filter/viewport=30.53995:30.06925:-97.44057:-98.05923,no-outline'
element = None

bot = Bot(url, driver)
address = 'San Marcos'


#Get the search button on the website and enter the address
bot.search_delay(2).wait(3).search_element(By.CLASS_NAME, 'search-input-box').get_element().send_keys(address)
bot.get_element().send_keys(Keys.ENTER)


click_option(bot)

#Wait for the 4 seconds and then search for the images. 
elements = bot.wait(4).search_elements(By.CLASS_NAME, 'bp-Homecard__Photo--image').get_element()


url = []
for element in elements:
    if(element.get_attribute('src') and ('http' in element.get_attribute('src'))):
        url.append(element.get_attribute('src'))

display = True
if(display == True):
    for ur in url:
        print(ur)
    

