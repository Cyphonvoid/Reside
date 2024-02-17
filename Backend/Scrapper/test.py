from redfin import RedfinBot
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from Server.Server import MultiClientServer
import threading


def launcher(address):
    
    bot = RedfinBot()
    #value = bot.get_images_on_address(address)
    value = bot.location('specific').address(address).get_response()
    print(value)



def launch_server(self, state):

    print("Enter your address: ", end="")
    address = input()
    bot = RedfinBot()
    #value = bot.get_images_on_address(address)
    value = bot.location('specific').address(address).get_response()
    
    if(state == True):
        server = MultiClientServer()
        server.load_messages(value)
        server.run('192.168.1.222', 9999)
        server.close()

    
print("Testing program has started: ")
flag = False
while(True):

    print(">> ", end="")
    var = input()

    if(var == 'launch'):
        print("Enter your address please: ", end="")
        val = input()
        launcher(val)

        if(flag == False):
            break
        
        time.sleep(4)
        launcher(val)
        time.sleep(4)
        launcher(val)
        time.sleep(4)
        launcher(val)
    
    elif(var == 'exit'):
        break

    elif(var == 'signin'):
        """
        user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
        "Mozilla/5.0 (iPhone14,3; U; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19A346 Safari/602.1",
        # Add more User-Agent strings as needed
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0"
        ]
        chrome_options = Options()
        # Set the custom User-Agent
        chrome_options.add_argument(f"--user-agent={user_agents[2]}")
        driver = webdriver.Chrome(options=chrome_options)
        """

        driver = webdriver.Chrome()
        driver.get('https://redfin.com')
        time.sleep(60)
        driver.close()

    elif(var == 'redsignin'):
        driver = webdriver.Chrome()
        driver.get('https://redfin.com')
        time.sleep(50)
        pass
    

    elif(var == 'run server'):
        print("Enter State: ", end="")
        state = input()

        if(state == 'yes'):
            launch_server(True)
        else:
            launch_server(False)
    

