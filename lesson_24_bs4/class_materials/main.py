import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

user = UserAgent().random
url = 'https://browser-info.ru/'
headers = {
    'user-agent': user
}
response = requests.get(url, headers=headers)
html_page = response.text
# print(html_page)

soup = BeautifulSoup(html_page, 'lxml')
main_block = soup.find('div', id="tool_padding")
pl = main_block.find("div", id='plugins_list')
print(pl.text)
# block_js = main_block.find('div', id='javascript_check')
# list_elements = block_js.find_all('span')
# print(list_elements)
# js = list_elements[0].text
# status = list_elements[1].text
# print(f'{js} - {status}')
# Flash: отсутствует/выключен
# User-agent: значение


