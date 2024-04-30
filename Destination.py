import uuid

class Destination:
    def __init__(self, name, lattitude , longitude):
        self.name = name
        self.longitude = longitude
        self.lattitude = lattitude
        self.dest_id = self.generate_id()
    
    def generate_id(self):
        return str(uuid.uuid4())
    
    def print_arg(self):
            print("Name is : ",self.name)
            print("longitude is : ",self.longitude)
            print("lattitude is : ",self.lattitude)
            print(" destination id is : ",self.dest_id)