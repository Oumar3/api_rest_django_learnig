import requests

Endpoint = "http://127.0.0.1:8000/api/product"

re = requests.post(Endpoint,json={'name':'Ali','price':23})


print(re.json())
print(re.status_code)
