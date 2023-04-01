# import requests and random
import requests
import random

FILENAME = "test_features.txt"


def post_data_to_api(z_mean, z_variance, z_deviation, z_peak, z_low, latitude, longitude):
    # define the API endpoint
    url = 'http://10.10.25.70/RoadioApp_Server_Code/views/InsertRoadData_API.php?apicall=addRoadData'
    # define the data to be sent
    data = {
        'Z_Mean': z_mean,
        'Z_Variance': z_variance,
        'Z_Deviation': z_deviation,
        'Z_Peak': z_peak,
        'Z_Low': z_low,
        'latitude': latitude,
        'longitude': longitude
    }
    # send a POST request with the data
    response = requests.post(url, json=data)
    # check the response status code
    return response.json()


def generate_data(filename):
    # Open the file in read mode
    with open(filename, "r") as file:
        # Loop through each line in the file
        for line in file:
            # Sample of random latitude and longitude points for a bad roads- Based on the work of Francis
            rand_latitude_for_bad = random.uniform(-0.2369879, -0.22195925)
            rand_longitude_for_bad = random.uniform(5.73995398, 5.76542204)

            # Sample of random latitude and longitude points for a good roads- Based on the work of Francis
            rand_latitude_for_good = random.uniform(0.19214863, 0.27552346)
            rand_longitude_for_good = random.uniform(5.6180886, 5.68269272)

            # Remove the newline character from the end of the line
            line = line.strip()

            # Split the line using a comma as the delimiter
            line_items = line.split(",")

            # Extract each item in the line
            z_mean = float(line_items[0])
            z_variance = float(line_items[1])
            z_deviation = float(line_items[2])
            z_peak = float(line_items[3])
            z_low = float(line_items[4])
            grade_of_road = int(line_items[5])

            # If the grade of the road is less than 2, it is bad road, hence, we use the GPS range for the bad roads
            if grade_of_road <= int(2):
                print(post_data_to_api(z_mean, z_variance, z_deviation, z_peak, z_low, rand_latitude_for_bad,
                                       rand_longitude_for_bad))
            else:
                print(post_data_to_api(z_mean, z_variance, z_deviation, z_peak, z_low, rand_latitude_for_good,
                                       rand_longitude_for_good))


generate_data(FILENAME)
