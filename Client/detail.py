import requests

id = input("enter your id : ")

Endpoint = f"http://127.0.0.1:8000/api/product/{id}/detail/"

re = requests.get(Endpoint)


print(re.json())
print(re.status_code)
