import requests
detail_id = input("Please enter the ID which one you want to know about : ")
detail_id = int(detail_id)

endpoint = f"http://localhost:8000/api/products/{detail_id}/"

get_response = requests.get(endpoint)

print(get_response.json())

