import math
from Drivers import Drivers

class DriverHandler:
    def __init__(self):
        self.avaialbale_driver=[]
        self.enroute_drivers=[]

    
    def add_to_avaialble(self, driver):
        if driver in self.enroute_drivers:
            self.enroute_drivers.remove(driver)
        self.avaialbale_driver.append(driver)
    
    def add_to_enroute(self, driver):
        if driver in self.avaialbale_driver:
            self.avaialbale_driver.remove(driver)
        
        self.enroute_drivers.append(driver)
    def get_available_driver(self):
        return self.avaialbale_driver[0]
    def show_avaialbel_driver(self):
        print(self.avaialbale_driver)
    
    def show_enroute_driver(self):
        print(self.enroute_drivers)
    
    def remove_available_driver(self,driver):
        self.avaialbale_driver.remove(driver)
    
    def has_available_drivers(self):
        return len(self.avaialbale_driver) > 0
    def number_of_available_drivers(self):
        print("Number of available drivers : ",len(self.avaialbale_driver))

    def number_of_enroute_drivers(self):
        print("Number of enroute drivers : ",len(self.enroute_drivers))