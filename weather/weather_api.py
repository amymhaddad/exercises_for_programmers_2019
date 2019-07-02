import json
import requests


url = "http://api.openweathermap.org/data/2.5/weather"
params = {"APPID": "31422cb605846e0dcdd4f75cbe27cd38",}
headers = "Content-Type': 'application/json"


def get_user_city():
    """Get city name from user"""
    return input("What city are you in? ")

user_city = get_user_city()


def add_user_city_to_request_parameter(params, user_city):
    """Add user's city to the request parameter"""
    return params.setdefault('q', user_city.title())

add_user_city_to_request_parameter(params, user_city)



def find_weather_for_user_city():
    try: 
        response = requests.get(url, params)
        json_response = response.json()
        fahrenheit_temp = f"{(json_response['main']['temp'] * 9/5) - 459.67:.0f}"
    
    except KeyError as kerr:
        print(f"A {kerr} error has occurred.")
    
    except Exception as err:
        print(f"A {err} error has occurred.")
    
    else:
        return fahrenheit_temp
