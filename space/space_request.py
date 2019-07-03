"""Make an API request to get the names of people in space and the name of their spacecraft"""

import requests

response = requests.get(
    "http://api.open-notify.org/astros.json",
    headers={"Content-Type": "application/json"},
)
space_data = response.json()

space_people = [people["name"] for people in space_data["people"]]
spacecraft_name = [people["craft"] for people in space_data["people"]]
