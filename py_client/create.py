from getpass import getpass

import requests

auth_endpoint = "http://localhost:8000/api/auth/"
username = input("Your Username : ")
password = getpass("Your Password : ")

token_response = requests.post(auth_endpoint, json={"username": username, "password": password})
if token_response.status_code == 200:
    print(token_response.json())
    token = token_response.json()["token"]
    print(token)
    endpoint = "http://localhost:8000/api/products/"
    data = {"title": "new title is here"}
    headers = {
        "Authorization": f"Token {token}"
    }

    get_response = requests.post(endpoint, json=data, headers=headers)

    print(get_response.json())
print("your username or password are not matching")
