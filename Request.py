import uuid
from Riders import Riders
from Destination import Destination

class Requests:
    def __init__(self,rider, destination, buff_start, buff_reach ):
        self.rider = rider
        self.Destination = destination
        self.buff_start = buff_start
        self.buff_reach = buff_reach
        self.cost = None
        self.request_id = self.generate_id()

    def generate_id(self):
        return str(uuid.uuid4())
    
    def print_args(self):
        print("Reuest rider is ")
        self.rider.print_arg()
        print("Requested destination is ", self.Destination)
        print("Requested buffer time is between ",self.buff_start, " to ",self.buff_reach)
        print("Requested id is ", self.request_id)
    
    def update_cost(self, cost):
        self.cost = cost

# rider = Riders("Abhishek","IT","20124005")

# request = Requests(rider,"bus stand", "3:00 PM","5:00 PM")

# request.print_args()
