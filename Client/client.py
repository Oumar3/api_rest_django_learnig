import requests

Endpoint = "http://127.0.0.1:8000/api/"

re = requests.get(Endpoint)


print(re.json())
print(re.status_code)