# Carpooling System

## Overview
This repository contains an implementation of a carpooling system designed for a college environment. The system aims to reduce transportation costs for students by efficiently grouping them based on their travel destinations and departure times.

## Features
- Grouping students for carpooling based on destination and departure time.
- Maximizing the size of carpool groups to reduce per-person costs.
- Using the K Nearest Neighbors (KNN) algorithm to find nearest neighbors for grouping.
- Ensuring no duplication of requests in multiple carpools.
- Providing functionalities to add requests, calculate costs, and set the order of destinations.

## Algorithm Overview
1. **Grouping Requests**: 
    - Requests are grouped based on their departure and arrival times using a predefined time threshold.
    - Each group represents a potential carpool.

2. **KNN Grouping**:
    - For each group of requests, the KNN algorithm is applied to find nearest neighbors based on destination proximity.
    - The algorithm iterates through requests to find suitable carpool candidates using the KNN approach.

3. **Creating Carpools**:
    - Eligible carpools are identified based on the KNN results and time constraints.
    - Requests are added to carpools ensuring that no request is duplicated across multiple carpools.
    - If a carpool reaches its maximum capacity, it is moved to the list of full carpools.

4. **Calculate Time and Cost**:
    - Carpool departure time and buffer time are calculated based on the requests' arrival and departure times.
    - Costs for each request are calculated based on carpool size and distance traveled.

## Usage
1. **Adding Requests**:
    - Use the `add_request` or `add_requests` methods to add requests to the system.

2. **Grouping Requests**:
    - Call the `create_groups` method to group requests based on departure and arrival times.

3. **KNN Grouping**:
    - Apply the `knn_grouping` algorithm to find nearest neighbors for each request group.

4. **Creating Carpools**:
    - Use the eligible carpools list to create carpools based on KNN results and time constraints.

5. **Viewing Details**:
    - Call the `show_details` method on a carpool object to view its details, including associated requests.


