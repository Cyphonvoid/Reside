from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import random


class ZillowScript():

    def __init__(self, url, instance):
        self.url = url
        self.instance = instance


    def scrape(self):
        #get the url first
        self.instance.get(self.url)

        #Get the search field by some id and send the data into it
        try:
            time.sleep(4)
            try:
                search_field = self.instance.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/section/div[1]/div/form/div/div/div/input')
                search_field.send_keys("houston, texas")
                search_field.click()
            except Exception as e:
                pass

            time.sleep(5)
        except Exception as error:
            print("Error:", error)
        
        time.sleep(5)
        #Click on the search button
        
    def close(self):
        self.instance.quit()

    def set_url(self, url):
        self.url = url


# Initialize the WebDriver with Chrome options
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    "Mozilla/5.0 (iPhone14,3; U; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19A346 Safari/602.1",
    # Add more User-Agent strings as needed
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0"

]
# Set up Chrome options
chrome_options = Options()
#chrome_options.add_argument("--headless")

# Set the custom User-Agent
chrome_options.add_argument(f"--user-agent={user_agents[4]}")

url = ['https://www.youtube.com/', 'https://www.zillow.com/homes/for_rent/', 'https://www.zillow.com', 'https://whatu.info/', 'https://www.zillow.com/houston-tx/rentals/']
Driver = webdriver.Chrome(options=chrome_options)

scraper = ZillowScript(url[2], Driver)
scraper.scrape()


    

