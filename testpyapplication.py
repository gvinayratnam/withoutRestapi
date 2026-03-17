import requests
BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'apiJsonCBV'
res = requests.get(BASE_URL+ENDPOINT)
# print(res.json())
# print(type(res))
# print(type(res.json()))
data = res.json()
# print(data['eno'])
print(data)