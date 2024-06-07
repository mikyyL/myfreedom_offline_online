import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

url = 'https://github.com/login'
auth_url = 'https://github.com/session'
user = UserAgent().random

data = {
    'login': 'mikyedit@gmail.com',
    'password': 'artym_0107',
    'authenticity_token': ''
}
headers = {
    'user-agent': user
}

with requests.Session() as session:
    response = session.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    auth_token = soup.find('input', {'name': 'authenticity_token'})
    data['authenticity_token'] = auth_token['value']

    response = session.post(auth_url, headers=headers, data=data)
    html_page = response.text

    with open('github.html', 'w') as file:
        file.write(html_page)

