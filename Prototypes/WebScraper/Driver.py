from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder



class State():
    def __init__(self, default):
        self.state = default
    
    def set_true(self):
        self.state = True
    
    def set_false(self):
        self.state = False
    
    def check(self):
        return self.state


class DriverInstance():

    def __init__(self):
        self.status = State(False)
        self.instance = None
        self.spawn_count = 0
        self.spawn_limit = 1
    
    def instance(self):
        return self.instance

    def activate(self):
        self.status.set_true()
        return self

    def create(self):
        if(self.status.check() == False):
            return
        
        if(self.spawn_count < self.spawn_limit):
            self.instance = webdriver.Chrome()
            self.spawn_count += 1

        else:
            print("Can't create anymore instances")

    def close_window(self):
        self.instance.quit()
        
    def close_tab(self):
        self.instance.close()



Driver = DriverInstance()
Driver.activate()
Driver.create()
        
    
