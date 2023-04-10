# import requests and random
import requests
import random

FILENAME = "berekuso_road_datapoints.txt"


def post_data_to_api(z_mean, z_variance, z_deviation, z_peak, z_low, latitude, longitude):
    # define the API endpoint
    url = 'http://10.10.25.35/RoadioApp_Server_Code/APIs/InsertRoadData_API.php?apicall=addRoadData'
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
            rand_latitude = float(line_items[5])
            rand_longitude = float(line_items[6])

            # Post data to API
            print(post_data_to_api(z_mean, z_variance, z_deviation, z_peak, z_low, rand_latitude, rand_longitude))


generate_data(FILENAME)
