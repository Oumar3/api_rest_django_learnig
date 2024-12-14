import requests

id = input("enter your id : ")

Endpoint = f"http://127.0.0.1:8000/api/product/{id}/update/"

re = requests.put(Endpoint,json={"name":"Cahier","price":500})


print(re.json())
print(re.status_code)
