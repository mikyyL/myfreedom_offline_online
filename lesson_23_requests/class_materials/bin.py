import requests
from fake_useragent import UserAgent

# user = UserAgent().random
# headers = {
#     'Accept': 'application/json',
#     'User-agent': user
# }
# url = "https://httpbin.org/headers"
#
# response = requests.get(url, headers=headers, timeout=6)
# print(response.json())

# url = 'https://httpbin.org/post'
# data = {
#     'custname': 'Artem',
#     'custtel': '1235356',
#     'custemail': 'root@gmail.com',
#     'size': 'small',
#     'topping': 'bacon',
#     'delivery': '21:00',
#     'comments': 'faster'
# }
# user = UserAgent().random
# headers = {
#     'User-agent': user
# }
# response = requests.post(url, headers=headers, json=data)
# print(response.status_code)
# print(response.json())

url = "https://reqres.in/api/users?page=2"
response = requests.get(url)
print(response.status_code)
print(response.json())

# create

data = {
    "name": "morpheus",
    "job": "leader"
}
url = "https://reqres.in/api/users"
response = requests.post(url, json=data)
print(response.status_code)
print(response.json())



# # delete
url = f"https://reqres.in/api/users/{response.json()['id']}"
response = requests.delete(url)
print(response.status_code)


# url = "https://reqres.in/api/users?page=2"
# response = requests.get(url)
# print(response.status_code)
# print(response.json())


