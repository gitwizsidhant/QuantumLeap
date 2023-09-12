import requests
import json

city = input("Enter the name of the city: ")

url = f"https://api.weatherapi.com/v1/current.json?key=4e26bb3b843141a293a160717230909&q={city}"

r = requests.get(url)

dic = json.loads(r.text)

import pyttsx3
try:
    engine = pyttsx3.init()
    engine.say(f"The current weather in {city}, {dic['location']['region']}," 
                f"{dic['location']['country']} is {dic['current']['temp_c']} degrees" 
                f"and it was last updated at {dic['current']['last_updated']},"
                f"with wind speed {dic['current']['wind_mph']}and {dic['current']['wind_kph']},"
                f" with a humitity of {dic['current']['humidity']} and wind direction is"
                f"{dic['current']['wind_dir']}")
    engine.runAndWait()

except Exception as e:
    print("Some error occured: ", e)