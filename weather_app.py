import requests

api_key = 'a54f5e809d19b466ea9473efa696d098'

city = raw_input('Enter city name: ')

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(city, api_key)

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    desc = data['weather'][0]['description']
    print('Temperature: {} K'.format(temp))
    print('Description: {}'.format(desc))
else:
    print('Error fetching weather data')
