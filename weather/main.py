"""A program that finds the current weather for any city in the world in Fahrenheit."""

from weather_management import find_weather_for_user_city


def get_local_weather():
    """Return a city's current weather based on user's input"""

    temp_kelvin = find_weather_for_user_city()
    fahrenheit_temp = f"{(temp_kelvin['main']['temp'] * 9/5) - 459.67:.0f}"

    print(fahrenheit_temp)


if __name__ == "__main__":
    get_local_weather()
