import requests
import json

url = 'https://fake-json-api.mock.beeceptor.com/users'
response = requests.get(url)

code = response.status_code
assert code == 200

data = response.json()

for item in data:
    if int(item['id']) == 10:  # Ensure id is compared as an integer
        print(f"ID 10 name: {item['name']}")
