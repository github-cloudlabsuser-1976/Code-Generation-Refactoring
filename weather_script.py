def get_weather(api_url, api_key, location):
    """
    Fetches weather data from the API for a given location.

    Parameters:
    api_url (str): The base URL of the weather API.
    api_key (str): The API key for authentication.
    location (str): The location for which to fetch the weather data.

    Returns:
    dict: The weather data for the given location.
    """
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

if __name__ == "__main__":
    API_URL = "https://api.openweathermap.org/data/2.5/weather"
    API_KEY = "3131d7fe17853b9e4b94cb7695637752"  # Your provided API key
    LOCATION = "London"

    try:
        weather_data = get_weather(API_URL, API_KEY, LOCATION)
        print(f"Weather in {LOCATION}:")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Weather: {weather_data['weather'][0]['description']}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")