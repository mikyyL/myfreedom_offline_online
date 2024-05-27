import requests

url = "https://api.openweathermap.org/data/2.5/weather"
API_TOKEN = '4cbadaaa44e5845a2e5ab66dad7b1cbe'
params = {'q': 'Минск', 'appid': API_TOKEN, 'units': 'metric'}
response = requests.get(url, params=params)
# print(response.status_code)
# print(response.headers)
print(response.json())
# print(type(response.text))
# temp_min, temp_max, country, name, speed