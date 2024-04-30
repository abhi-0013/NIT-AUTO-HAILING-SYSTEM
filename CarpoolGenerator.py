from math import radians, sin, cos, sqrt, atan2
from RequestHandler import RequestHandler
from DriverHandler import DriverHandler
from Carpool import Carpool


class CarpoolGenerator:
    def __init__(self, request_handler, driver_handler):
        self.request_handler = request_handler
        self.driver_handler = driver_handler
        self.available_carpools = []
        self.full_carpools = []

    def calculate_distance(self, destination1, destination2):
        # Calculate the distance between two destinations using Haversine formula
        R = 6371.0  # Earth radius in kilometers

        lat1 = radians(float(destination1.lattitude))
        lon1 = radians(float(destination1.longitude))
        lat2 = radians(float(destination2.lattitude))
        lon2 = radians(float(destination2.longitude))

        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = R * c

        return distance

  
    def knn_grouping(self, requests, threshold_distance, max_group_size, eligible_carpools):
    # Initialize an empty list to store grouped carpools
        carpools = []
        
        # Initialize an empty set to keep track of request IDs that have been added to a carpool
        added_request_ids = set()

        # Loop through requests to find nearest neighbors
        for request in requests:
            
            # Check distance between new request and each request in the group

            # Check if the new request can be added to eligible carpools
            for carpool in eligible_carpools:
                if all(self.calculate_distance(request.Destination, carpool_request.Destination) < threshold_distance
                    for carpool_request in carpool):
                    # nearest_requests.extend(carpool)
                    if len(carpool.Request) + 1 <= max_group_size:
                        carpool.add_request(request)
                    # Add request IDs of the carpool's requests to the set of added request IDs
                        added_request_ids.add(request.request_id)
                        break
                    else:
                        self.full_carpools.append(carpool)
                        self.available_carpools.remove(carpool)

        for request in requests:
            if request.request_id not in added_request_ids:
                min_distance = float('inf')
                nearest_requests = []
                for other_request in requests:
                    if other_request.request_id not in added_request_ids:
                        distance = self.calculate_distance(request.Destination, other_request.Destination)
                        if distance < threshold_distance:
                            nearest_requests.append(other_request)
                            min_distance = min(min_distance, distance)
                    
                for carpool in eligible_carpools:
                    if all(self.calculate_distance(request.Destination, carpool_request.Destination) < threshold_distance
                        for carpool_request in carpool.Request):
                            # nearest_requests.extend(carpool)
                        nearest_requests.extend(carpool)
                            # Add request IDs of the carpool's requests to the set of added request IDs
                        eligible_carpools.remove(carpool) 
                        added_request_ids.update(request.request_id for request in nearest_requests)

                if len(nearest_requests) + 1 <= max_group_size:
                    nearest_requests.append(request) # to add the curretn request
                    added_request_ids.update(request.request_id for request in nearest_requests)
                    cp = Carpool(None, None,None)
                    cp.add_requests(nearest_requests)
                    eligible_carpools.append(cp)
                else:
                    ## here write the code that will divide the carpool into carpools of smaller size
                    nearest_requests.append(request)
                    number_of_new_carpools = len(nearest_requests) / max_group_size
                    for i in range(1, number_of_new_carpools+1):
                        cp = Carpool(None, None,None)
                        cp.add_requests(nearest_requests[(i-1)*max_group_size:i*max_group_size ])
                        added_request_ids.update(nearest_requests[(i-1)*max_group_size:i*max_group_size ])
                        eligible_carpools.append(cp)
                    cp = Carpool(None,None,None)
                    cp.add_requests(nearest_requests[number_of_new_carpools*max_group_size:])
                    added_request_ids.update(nearest_requests[number_of_new_carpools*max_group_size:])
                    eligible_carpools.append(cp)

        return eligible_carpools


    def divide_into_carpools(self):
        groups = self.request_handler.get_groups()
        threshold_distance = 2  # Threshold for proximity in kilometers
        max_group_size = 8  # Maximum members allowed in a carpool

        for group in groups:
            # Initialize a list to store existing carpools that meet the criteria
            eligible_carpools = []

            # Find existing carpools that satisfy the time constraints for this group
            for carpool in self.available_carpools:
                if float(carpool.depart_time) >= max(float(request.buff_start) for request in group) and \
                        float(carpool.depart_time) < min(float(request.buff_reach) for request in group):
                    eligible_carpools.append(carpool)

            # Grouping based on KNN algorithm
            grouped_carpools = self.knn_grouping(group, threshold_distance, max_group_size,eligible_carpools)

            # Allocate drivers to carpools if available
            for carpool in grouped_carpools:
                if self.driver_handler.has_available_drivers():
                    driver = self.driver_handler.get_available_driver()
                    carpool_instance = Carpool(driver=driver, departure_time=max(request.buff_start for request in group),
                                               buff_time=min(request.buff_reach for request in group))
                    for request in carpool.Request:
                        carpool_instance.add_request(request)
                    self.driver_handler.remove_available_driver(driver)

                    # Update available and full carpools lists
                    if len(carpool_instance.Request) < max_group_size:
                        self.available_carpools.append(carpool_instance)
                    else:
                        self.full_carpools.append(carpool_instance)

        # Print information about generated carpools
        print("Available Carpools:")
        for i, carpool in enumerate(self.available_carpools):
            print(f"Carpool {i + 1}: {len(carpool.Request)} riders, Driver: {carpool.driver.name if carpool.driver else 'Unassigned'}")
            carpool.show_details()
            print("---------------")
            print()

        print("\nFull Carpools:")
        for i, carpool in enumerate(self.full_carpools):
            print(f"Carpool {i + 1}: {len(carpool.Request)} riders, Driver: {carpool.driver.name if carpool.driver else 'Unassigned'}")
            carpool.show_details()
            print("---------------")
            print()