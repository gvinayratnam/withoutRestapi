import requests
import json
BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'getall'
# res = requests.get(BASE_URL+ENDPOINT)
# print(res.json())
# print(type(res))
# print(type(res.json()))
# res = requests.post(BASE_URL+ENDPOINT)
# res = requests.put(BASE_URL+ENDPOINT)
# res = requests.delete(BASE_URL+ENDPOINT)


# data = res.json()
# print(data['eno'])
# print(data)

def create_data():
    emp_data = {
        'eno': 148,
        'ename' : 'sathish',
        'esal' : 500,
        'eadd' :'jgdjgshjg'
    }
    res = requests.post(BASE_URL+ENDPOINT,data = json.dumps(emp_data))
    print(res.json())
    print(res.status_code)
# create_data()


def update_data(id):
    ENDPOINT='apicurd/'
    emp_data = {
        'ename' : 'Rajesh Rao',
        'esal' : 500000,
    }
    res = requests.put(BASE_URL+ENDPOINT+str(id),data = json.dumps(emp_data))
    print(res.json())
    print(res.status_code)
update_data(6)