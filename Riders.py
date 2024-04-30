import uuid

class Riders:
    def __init__(self, name, department, Rollno):

        self.name = name
        self.department = department
        self.Rollno = Rollno
        self.Rider_id = self.generate_id()

    def generate_id(self):
        return str(uuid.uuid4())

    def print_arg(self):
            print("Name is : ",self.name)
            print("Department is : ",self.department)
            print("ROll no is : ",self.Rollno)
            print("Rider id is : ",self.Rider_id)


    def get_location(self):
         # the below function is used to get the location of the student
         pass

