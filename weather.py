import requests


def weatherMood():
    weather = requests.get("http://api.openweathermap.org/data/2.5/weather?zip=94108,us&appid=48b7a5079c5920a0bb7a4b60dde5b970")
    weather = weather.json()

    print("The current weather at Nob Hill is", weather["weather"][0]["description"])
    mood = input("What is your current mood: ")
    print("thanks for responding :)")

weatherMood()