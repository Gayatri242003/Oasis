import requests

def get_weather(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def display_weather(weather_data):
    if weather_data["cod"] == 200:
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        weather_conditions = weather_data["weather"][0]["description"]

        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather Conditions: {weather_conditions}")
    else:
        print("Failed to fetch weather data. Please check the location.")

def main():
    api_key = "faaa48703941c7f374e33ff15fdafad5"
    location = input("Enter the city name or ZIP code: ")
    weather_data = get_weather(api_key, location)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
