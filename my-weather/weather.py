import requests

# Set your API key and default city
api_key = 'a54f5e809d19b466ea9473efa696d098'
default_city = 'New York'

# Prompt the user for a city name or keep the default
user_input = input('Enter a city name (or press Enter to keep "{}"): '.format(default_city))
city = user_input if user_input else default_city

# Construct the API URL
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(city, api_key)

# Send a request to the OpenWeatherMap API
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    desc = data['weather'][0]['description']
    print('Temperature: {} K'.format(temp))
    print('Description: {}'.format(desc))
else:
    print('Error fetching weather data')

