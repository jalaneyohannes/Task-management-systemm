import requests

def get_weather(api_key, city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Use Celsius for temperature
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error fetching weather data:", response.status_code)
        return None

def display_weather(data):
    if data is not None:
        print("\nCurrent Weather in", data['name'])
        print("Weather:", data['weather'][0]['description'])
        print("Temperature:", data['main']['temp'], "°C")
        print("Humidity:", data['main']['humidity'], "%")
        print("Wind Speed:", data['wind']['speed'], "m/s")
    else:
        print("No weather data available.")

def main():
    api_key = "YOUR_OPENWEATHERMAP_API_KEY"
    city = input("Enter city name: ")
    
    weather_data = get_weather(api_key, city)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
