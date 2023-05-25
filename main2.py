import requests
from datetime import datetime, timedelta

# Use https://www.latlong.net/ to get latitude and longitude of desired location

MY_LATITUDE = 36.750671
MY_LONGITUDE = -95.944389


def get_UTC_time():
    """
    Retrieves sunrise and sunset times of a specified latitude and longitude

    Returns:
        Sunset and Sunrise times in UTC
    """

    URL = "https://api.sunrise-sunset.org/json"

    parameters = {
        "lat": MY_LATITUDE,
        "lng": MY_LONGITUDE
    }

    # Get json data from url
    response = requests.get(url=URL, params=parameters)    
    response.raise_for_status()
    data = response.json()
    # print(data)

    # Parse json to get sunrise and sunset times
    sunset = data['results']['sunset']
    sunrise = data['results']['sunrise']    

    return sunset, sunrise


def convert_UTC_to_CST():    
    """
    Converts time in UTC to CST

    Calculation:
        CST = UTC - 5

    Returns:
        Sunset and Sunrise times in CST
    """
    sunset, sunrise = get_UTC_time()

    # Parse strings into datetime objects
    sunset_object = datetime.strptime(sunset, "%I:%M:%S %p")
    sunrise_object = datetime.strptime(sunrise, "%I:%M:%S %p")

    # Convert time from UTC to CST
    sunrise_conversion = sunrise_object - timedelta(hours=5)
    sunset_conversion = sunset_object - timedelta(hours=5)

    # Format datetime object into desired format
    sunrise_time = sunrise_conversion.strftime("%I:%M:%S %p")
    sunset_time = sunset_conversion.strftime("%I:%M:%S %p")

    print("Sunrise time:", sunrise_time)
    print("Sunset time:", sunset_time)    
    
    return sunrise_time, sunset_time

print(convert_UTC_to_CST())



