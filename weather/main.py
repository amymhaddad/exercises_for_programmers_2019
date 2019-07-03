"""A program that finds the current weather for any city in the world in Fahrenheit."""

from weather_management import find_weather_for_user_city, convert_kelvin_to_fahrenheit
from user_input import get_user_city


def main():
    """Return a city's current weather based on user's input"""
    #input
    city = get_user_city()

    #logic
    kelvin_temperature = find_weather_for_user_city(city)
    fahrenheit_temperature = convert_kelvin_to_fahrenheit(kelvin_temperature)

    #printing
    print(fahrenheit_temperature)

if __name__ == "__main__":
    main()
