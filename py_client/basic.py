import requests

endpoint = "http://localhost:8000/api/"

get_response = requests.post(endpoint, params={"abc": 123}, json={"title": "this is a first title", "price": 555}, )
# print(get_response.text)
print(get_response.json())
# print(get_response.status_code)
# print(get_response.headers)
