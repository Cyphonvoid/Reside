from bot import Bot
from selenium import webdriver
from Utility import ObjectID, State
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

"""
Tasks based:
    - Search and load location
    - Managing Filters
    - Finding Images and Text data
    
"""

"""
Part based:
    - Search Component
    - Filter component
    - Image Component
    - Text Component
"""


INIT_URL = 'https://www.redfin.com/'
WEB_DRIVER = None

#In future, elements references can be chained kind of like action chains
class ElementReference():

    def __init__(self, tag, value):
        self.tag = tag
        self.tag_value = value
    
    def set_reference(self, tag, value):
        self.tag=tag
        self.tag_value = value

    def find_self(self):
        pass

    def define_action(self):
        pass

    def get_reference(self, name):
        if(name == 'By'):
            return self.tag
        
        elif(name == 'value'):
            return self.tag_value
        
        return False


class Listing():

    def __init__(self):
        self.address = None
        self.image_urls = []
        self.price = None
        self.property_stats = None
    
    def get_images(self):
        return self.image_urls

    def get_price(self):
        return self.price
    
    def get_stats(self):
        return self.property_stats
    
    def get_address(self):
        return self.address
    
    def export(self):
        pass

class FetchListings():

    def __init__(self):
        self.house_listings = []
        pass

    def fetch(self):

        pass



class HouseType():

    def __init__(self):
        self.main_button = ElementReference(By.XPATH, '/html/body/div[1]/div[8]/div[2]/div[1]/div[2]/div/div/div/div[1]/form/div[1]/div')
        self.for_rent = ElementReference(By.ID, 'forRent')
        self.for_sale = ElementReference(By.ID, 'for-sale')
        self.done_button = ElementReference(By.XPATH, '/html/body/div[1]/div[8]/div[2]/div[1]/div[2]/div/div/div/div[1]/form/div[1]/div/div[2]/div/div[2]/button')

    def get_main(self):
        return self.main_button

    def get_sub_filter(self, choice):
        if(choice == 'for sale'):
            return self.for_sale
        elif(choice == 'for rent'):
            return self.for_rent
        

class RedfinSearch():

    def __init__(self, bot):
        self.bot = bot
        self._id = ObjectID('redfin search', 2000)
        self.status = State()
        self.location_address = None
        self.search_element = ElementReference(By.CLASS_NAME, 'search-input-box')
        self.property_type = HouseType()
        self.filter = None

    def __task(self):
        #Search for the address and click okay
        element = self.bot.wait(4).search_element(self.search_element.get_reference('By'), self.search_element.get_reference('value')).get_element()
        element.send_keys(self.location_address)
        element.send_keys(Keys.ENTER)
        self.bot.wait(4)
        

        if(self.filter != None):
            #Apply the filters
            #Click on house filter
            path = '/html/body/div[1]/div[8]/div[2]/div[1]/div[2]/div/div/div/div[1]/form/div[1]/div'
            main = self.property_type.get_main()
            self.bot.search_element(main.get_reference('By'), main.get_reference('value')).get_element().click()

            if(self.filter == 'for rent'):
                #Select the rent option
                button = self.property_type.get_sub_filter('for rent')
                self.bot.wait(0.5).search_element(button.get_reference('By'), button.get_reference('value')).get_element().click()
            
            elif(self.filter == 'for sale'):
                #Select the rent option
                button = self.property_type.get_sub_filter('for sale')
                self.bot.wait(0.5).search_element(button.get_reference('By'), button.get_reference('value')).get_element().click()

            #Click on done
            path = '/html/body/div[1]/div[8]/div[2]/div[1]/div[2]/div/div/div/div[1]/form/div[1]/div/div[2]/div/div[2]/button'
            self.bot.search_element(By.XPATH, path).get_element().click()
            self.bot.wait(3)
    
    def set_location_address(self, address):
        if(isinstance(address, str)):
            self.location_address = address
    
    def apply_filter(self, filter):
        self.filter = filter

    def perform(self):
        self.__task()
        pass

    def id(self):
        return self._id


class Tasks():

    def __init__(self):
        self.task_list = []

    def get(self, index):
        try:
            return self.task_list[index]
        except Exception as error:
            return False


    def search(self, id):
        for task in self.task_list:
            if(task.id().get('name') == id):
                return task       
        return False

    def add(self, task):
        self.task_list.append(task)
    
    def pop(self, index):
        self.task_list.pop(index)
    
    def get_total_tasks(self):
        return len(self.task_list)
        
    def run(self, tag):
        if(tag == 'all'):
            for task in self.task_list:
                task.perform()
            return 
        
        elif(isinstance(tag, int) == True):
            try:
                self.task_list[tag].perform()
                return True
            except Exception as error:
                return False



class RedfinBot():

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.bot = Bot(INIT_URL, self.driver)
        self.tasks = Tasks()
        self.redfin_search = RedfinSearch(self.bot)

        self.bot.activate()

    def get_images_on_address(self, address, filter=None):
        self.redfin_search.set_location_address(address)
        if(filter != None): self.redfin_search.apply_filter(filter)
        self.redfin_search.perform()
        pass

    def get_text(self):
        pass
    
    def run(self):
        self.tasks.run()

    def stop(self):
        pass
    pass

bot = RedfinBot()
bot.get_images_on_address('San Marcos', 'for sale')