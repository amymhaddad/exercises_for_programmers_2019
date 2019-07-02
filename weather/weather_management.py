"""Try to make API call based on user input"""

from user_input import get_user_city
import requests
import json

url = "http://api.openweathermap.org/data/2.5/weather"
params = {"APPID": "31422cb605846e0dcdd4f75cbe27cd38"}
headers = {"Content-Type": "application/json"}

def add_user_city_to_request_parameter(params):
    """Add user's city to the request parameter"""
    user_city = get_user_city()
    params.setdefault("q", user_city.title())
    return params


def find_weather_for_user_city():
    """Get the temperature for a city in Kelvin. Raise an error is city doesn't exist."""
    try:
        params_with_city = add_user_city_to_request_parameter(params)
        response = requests.get(url, params_with_city)
        json_response = response.json()
        
    except KeyError as kerr:
        print(f"A {kerr} error has occurred.")

    except Exception as err:
        print(f"A {err} error has occurred.")

    else:
        return json_response
