"""Try to make API call based on user input"""

import requests

APPID = "31422cb605846e0dcdd4f75cbe27cd38"

def find_weather_for_user_city(city):
    """Get the temperature for a city in Kelvin. Raise an error is city doesn't exist."""

    params = {
        'APPID': APPID,
        'q': city,
    }

    headers = {
        "Content-Type": "application/json"
        }

    try:
        response = requests.get(
            "http://api.openweathermap.org/data/2.5/weather",
            params=params,
            headers=headers,
        )
        json_response = response.json()

    except KeyError as kerr:
        print(f"A {kerr} error has occurred.")

    except Exception as err:
        print(f"A {err} error has occurred.")

    else:
        return json_response

def convert_kelvin_to_fahrenheit(kelvin_temperature):
    """Convert the weather from Kelvin to Fahrenheit"""
    return f"{(kelvin_temperature['main']['temp'] * 9/5) - 459.67:.0f}"
