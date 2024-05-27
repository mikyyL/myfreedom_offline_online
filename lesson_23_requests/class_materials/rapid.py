import requests

url = "https://google-translate1.p.rapidapi.com/language/translate/v2/detect"
headers = {
    "content-type": "application/x-www-form-urlencoded",
    "Accept-Encoding": "application/gzip",
    "X-RapidAPI-Key": '46a60ddcfamsh735cfd849f48005p1f6015jsn9acf1c534c5d',
    "X-RapidAPI-Host": 'google-translate1.p.rapidapi.com'
}
data = {
    'q': 'Привет'
}
response = requests.post(url, headers=headers, data=data)
print(response.json())
