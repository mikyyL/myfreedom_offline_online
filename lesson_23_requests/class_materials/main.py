import requests

params = {'q': 'python'}
response = requests.get("https://www.google.com/search", params=params)
# print(response)
# print(response.status_code)
# print(response.headers)
# print(response.text)

with open('google.html', 'w', encoding='utf-8') as file:
    file.write(response.text)