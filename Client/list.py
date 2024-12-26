import requests
from getpass import getpass

Endpoint_auth = "http://127.0.0.1:8000/api/auth/"

username = input("Entrez votre username : ")
password = getpass("Entrez votre password : ")

auth_response = requests.post(Endpoint_auth, json={"username":username,"password":password})
print(auth_response.json())

if auth_response.status_code==200:

    headers = {
        "Authorization": "Token 119b25da8ec216e9ccff7eb8242f4dcd81313b46"
    }

    Endpoint = "http://127.0.0.1:8000/api/product/create-product/"


    re = requests.get(Endpoint,headers=headers)


    print(re.json())
    print(re.status_code)
