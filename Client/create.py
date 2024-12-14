import requests

Endpoint = "http://127.0.0.1:8000/api/product/create-product/"

re = requests.post(Endpoint,json={"name":"Velo","price":1000})


print(re.json())
print(re.status_code)
