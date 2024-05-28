import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

user = UserAgent().random
url = "https://www.21vek.by/mobile/iphone_15pro/"
headers = {
    'user-agent': user
}
response = requests.get(url, headers=headers)
# with open('21vek.html', 'w') as file:
#     file.write(response.text)

soup = BeautifulSoup(response.text, 'lxml')
main_block = soup.find('div', {'data-testid': 'product-list'})
print(main_block)
# первый телефон
block_phone = main_block.find('div', {"data-testid": 'product-8560605'})
# print(block_phone)
block_phone_2 = block_phone.find('p', {"data-testid": 'card-info'})
# print(block_phone_2)
title_phone = block_phone_2.find('a', {'data-testid': 'card-info-a'}).text
# print(title_phone)
# price
block_price = block_phone.find('section', {'data-testid': 'card-price'})
# print(block_price)
price = block_price.find('p', {"data-testid": 'card-current-price'}).text
print(title_phone, price)
# a=0
# Смартфон Apple iPhone 15 Pro 256GB - 3 - отзыва - 4 899,00 р.

# Второй телефон
block_phone = main_block.find('div', {"data-testid": 'product-8560616'})
print(block_phone)
vote = block_phone.find('a', {"draggable": 'true'}).text
print(vote)
# block_delivery = block_phone.find('span', {"data-testid": 'card-container'})
# print()

