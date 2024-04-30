import uuid

class Drivers:
    def __init__(self,name, Rickshaw_No, mobile_number):
        self.name = name
        self.Rickshaw_No = Rickshaw_No
        self.mobile_number = mobile_number
        self.Driver_id = self.generate_id()

    def generate_id(self):
        return str(uuid.uuid4())
    
    def print_args(self):
        print("Driver name is ", self.name)
        print("Driver plate number is ", self.Rickshaw_No)
        print("Driver mobile number is ", self.mobile_number)
        print("Driver id is ", self.Driver_id)

    def get_location(self):
        #this below function is used for getting the driver location
        pass