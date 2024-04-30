import uuid
from Request import Requests
from Drivers import Drivers
from Riders import Riders
from Destination import Destination


class Carpool:
    def __init__(self, driver, departure_time, buff_time):
        self.driver = driver
        self.depart_time = departure_time
        self.buff_time = buff_time
        self.Request = []
        self.carpool_id = self.generate_id()
    
    def generate_id(self):
        return str(uuid.uuid4())
    
    def calculate_time(self):
        if not self.Request:
            return
        
        min_buff_reach = min(float(request.buff_reach) for request in self.Request)
        self.depart_time = (min_buff_reach - 0.25) if min_buff_reach >= 0.25 else (24 + min_buff_reach - 0.25)
        
        max_buff_start = max(float(request.buff_start) for request in self.Request)
        self.buff_time = (self.depart_time - 0.5) if (self.depart_time - 0.5) >= max_buff_start else max_buff_start

    def add_request( self , request):
        self.Request.append(request)
    
    def add_requests(self, request):
        self.Request.extend(request)

    def show_details(self):
        print("Carpool ID:", self.carpool_id)
        print("Driver:", self.driver)
        print("Departure Time:", self.depart_time)
        print("Buffer Time:", self.buff_time)
        print("Requests:")
        for request in self.Request:
            print("RIder is : ",request.rider.name," Destination is : ",request.Destination.name)
            print("******")
            print()    
    def calculate_cost(self, request):
        # calculates the cost of the request based on the size of the carpool 
        # and total distance travelled by the auto and destiantion
        pass

    def calculates_total_distance(self):
        # this function finds the shorted path returns the distance
        pass

    def set_order_of_destiantion(self):
        # this function make the requests in order of its travel routine
        pass