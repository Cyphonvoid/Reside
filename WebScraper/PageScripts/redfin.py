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


url = 'https://www.redfin.com/city/30818/TX/Austin'

def click_next_page():
    pass
"""
  for i in range(0, times):
        try:
            image_element = driver.find_element(By.CLASS_NAME, class_name)

            if((image_element.get_attribute('src')) and 'http' in image_element.get_attribute('src')):
                image_urls.append(image_element.get_attribute('src'))
            else:
                print("ERROR: Image found but has no http url or src tag inside it")
        except Exception as error:
            print("Error:", error)
        
        time.sleep(1)
    """

def search_images_on_redfin(url, driver, times):
    class_name = 'bp-Homecard__Photo--image'
    driver.get(url)
    image_urls = []

    images = driver.find_elements(By.CLASS_NAME, class_name)
    
    for image in images:
        print(image.get_attribute('src'))

    return image_urls


def open_image_online(driver):

    file = open("C:\\Users\\yasha\\Visual Studio Workspaces\\SystemX\\Reside\\WebScraper\\PageScripts\\image_urls.txt", "r")

    for i in range(0, 20):
        line = file.readline()
        print(line)
        driver.get(line)
        time.sleep(0.4)


def download_and_save_images(url_array):
    for i in range(0, len(url_array)):
        try:
            name = "C:\\Users\\yasha\\Visual Studio Workspaces\\SystemX\\Reside\\WebScraper\\PageScripts\\images" + "\\image" + str(i) + ".jpeg"
            file = open(name, "w")
            time.sleep(0.2)
            file.close()

        except Exception as error:
            pass

    num = 0

    for url in url_array:
        try:
        
            #download the image now
            image_content = requests.get(url).content
            image_file = io.BytesIO(image_content)
            image = Image.open(image_file)

            #split the url and get the last name 
            #image_name = url.split('/')[-1]
            directory = "C:\\Users\\yasha\\Visual Studio Workspaces\\SystemX\\Reside\\WebScraper\\PageScripts\\images" + "\\image" + str(num) + ".jpeg"
            with open(directory, "wb") as f:
                image.save(f, "JPEG")

            num += 1
        except Exception as error:
            print(error, "Error: Couldn't create file!")

#https://ssl.cdn-redfin.com/system_files/media/890870_JPG/genDesktopMapHomeCardUrl/item_21.jpg
driver = webdriver.Chrome()
#array = search_images_on_redfin(url, driver, 7)
#print(array)
#download_and_save_images(array)
open_image_online(driver=driver)

        




    