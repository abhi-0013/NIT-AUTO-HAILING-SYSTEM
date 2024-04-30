import math
from Request import Requests
from Drivers import Drivers
from Riders import Riders
from Destination import Destination

class RequestHandler:
    def __init__(self ):
        self.available =[]
        self.carpool = {}
        self.availble_groups=[]
        
    def add_Request(self, request):
        self.available.append(request)
    
    def add_to_carpool(self, request):
        pass

    def create_groups(self):
        sorted_requests = sorted(self.available, key=lambda x: x.buff_reach)
        self.availble_groups
        # Iterate through sorted requests
        for request in sorted_requests:
            allocated = False

            # Try to add request to an existing group
            for group in self.availble_groups:
                # Check if adding request to the group violates condition
                if group[0].buff_reach > request.buff_start:
                    group.append(request)
                    allocated = True
                    break

            # If request cannot be added to any existing group, create a new group
            if not allocated:
                self.availble_groups.append([request])

    def get_groups(self):
        return self.availble_groups

    
    def show_groups(self):
        for i, group in enumerate(self.availble_groups):
            print(f"Group {i + 1}: {[f'(Start: {request.buff_start}, Reach: {request.buff_reach})' for request in group]}")




# just testing code


#  handler = RequestHandler()


# handler.add_Request(Requests(Riders("Abhishek1","IT","20124005",),Destination("Bus stand","31.3127° N", "75.5913° E"),"12","16"))
# handler.add_Request(Requests(Riders("Abhishek2","IT","20124006",),Destination("Bus stand","31.3127° N", "75.5913° E"),"13","15"))
# handler.add_Request(Requests(Riders("Abhishek3","IT","20124007",),Destination("Bus stand","31.3127° N", "75.5913° E"),"12","15"))
# handler.add_Request(Requests(Riders("Abhishek4","IT","20124008",),Destination("Bus stand","31.3127° N", "75.5913° E"),"14","18"))
# handler.add_Request(Requests(Riders("Abhishek5","IT","20124009",),Destination("Bus stand","31.3127° N", "75.5913° E"),"15","17"))
# handler.add_Request(Requests(Riders("Abhishek6","IT","20124015",),Destination("Bus stand","31.3127° N", "75.5913° E"),"12","14"))
# handler.add_Request(Requests(Riders("Abhishek7","IT","20124025",),Destination("Bus stand","31.3127° N", "75.5913° E"),"12","17"))
# handler.add_Request(Requests(Riders("Abhishek8","IT","20124035",),Destination("Bus stand","31.3127° N", "75.5913° E"),"13","16"))

# handler.create_groups()
# handler.show_groups()

