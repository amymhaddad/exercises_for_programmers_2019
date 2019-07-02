import json
import requests

response = requests.get(
    "https://api.openweathermap.org/data/2.5/weather", 
    params={"q": "London"},
    headers={"Content-Type": "text/html; charset=UTF-8"},    
    )


json_response = response.json()
print(json_response)