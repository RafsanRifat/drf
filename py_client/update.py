from getpass import getpass

import requests

username = input("your username : ")
password = getpass("your password : ")
auth_endpoint = "http://localhost:8000/api/auth/"
auth_response = requests.post(auth_endpoint, json={"username": username, "password": password})
print(auth_response.json())
token = auth_response.json()['token']
print(token)


data = {
    "title": "updated title"
}

headers = {
        "Authorization": f"Token {token}"
    }
endpoint = "http://localhost:8000/api/products/1/update/"


get_response = requests.put(endpoint, headers=headers, json=data )

print(get_response.json())
