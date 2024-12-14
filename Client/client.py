import requests

Endpoint = "http://127.0.0.1:8000/api/product/"

re = requests.post(Endpoint,json={"name":"Livre","price":750})


print(re.json())
print(re.status_code)
