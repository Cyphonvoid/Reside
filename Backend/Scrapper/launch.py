from redfin import RedfinBot
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
#from Server.Server import MultiClientServer
import threading
from Client import WebClient
from http.server import HTTPServer, BaseHTTPRequestHandler


class Serve(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "Json")
        self.end_headers()
        self.param_list = []

        print("URL RECIEVED:", self.path)
        self.param_list = self.path.split('/')

        if('service' in self.param_list):
            index = self.param_list.index('service')
            index += 1

            try:
            
                string = self.param_list[index]
                param_list = []
                for i in range(0, len(string)):
                    param_list.append(string[i])

                p_str = ''
                for i in range(0, len(param_list)-1):
                    if(i > len(param_list)-1):break
                    if(param_list[i] == '%'):
                        if(param_list[i+1] == '2'):
                            param_list.pop(i+1)
                            param_list.pop(i+1)
                        param_list.pop(i)
                        param_list.insert(i, " ")
                    p_str += param_list[i]
                        

                print("AFTER FILTER: ", p_str)
                value = self.process_request(p_str)
                response = "{ 'message': " + str(value) + " }" 
                self.send_response(500)
                self.wfile.write(bytes(response, "utf-8"))
            
            except Exception as error:
                print(error)
                self.wfile.write(bytes("Address specified is nout found", "utf-8"))
        
        else:
            self.send_response(403)

    def process_request(self, address):
        bot = RedfinBot()
        #value = bot.get_images_on_address(address)
        value = bot.location('specific').address(address).get_response()
        return value
        pass


def launcher(address):
    bot = RedfinBot()
    #value = bot.get_images_on_address(address)
    value = bot.location('specific').address(address).get_response()
    print(value)


def launch_server():
    print("Enter your address: ", end="")
    address = input()
    if(address == 'exit'):
        return
    bot = RedfinBot()
    #value = bot.get_images_on_address(address)
    value = bot.location('specific').address(address).get_response()
    client = WebClient('Scrapper Bot')
    client.load_message(value)
    client.connect_to('192.168.1.183', 9999).run()
    print("test", client.get_card().read().name())
    client.close()



def launch_http():
    print("HTTP://192.168.222:9999   Started.....")
    server = HTTPServer(('192.168.1.222', 9999), Serve)
    server.serve_forever()
    server.server_close()

    pass


print("Testing program has started: ")
flag = True
while(True):

    print(">> ", end="")
    var = input()

    if(var == 'launch'):
        print("Enter your address please: ", end="")
        val = input()
        if(val == 'exit'):
            continue
        launcher(val)
    
    elif(var == 'http server'):
        launch_http()
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
    
    elif(var == 'run server'):
        launch_server()
    

