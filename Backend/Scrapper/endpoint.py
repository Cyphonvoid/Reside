import requests


class ScrapperAPI():

    def __init__(self):
        self.address = ''
        self.domain = None
        self.url = '/service/'
        self.lang_id = "/python"
    
    def get_listing_on_specific_address(self, address):
        if(self.domain == None):
            print("Domain wasn't selected")
            return
        #url = "http://" + self.domain + self.url + "/" + address
        url = "http://" + self.domain + self.url + address + self.lang_id
        return requests.get(url).text
    
    def destination_server(self, ip, port):
        self.domain = ip + ":" + str(port)
    
#
api  = ScrapperAPI()
api.destination_server('38.56.138.77', 8888)
print(api.get_listing_on_specific_address('1401 Union St,San Diego, CA'))
