import requests
import json

url = 'https://reqres.in/api/users?page=2'
response = requests.get(url)

assert response.status_code == 200
jsonObject = response.json()

print(jsonObject['page'])  # Prints the page number

# Accessing the first user's id from the 'data' list
host = jsonObject['data'][0]['id']
print(host)  # Prints the ID of the first user in the list
host = jsonObject['support']['url']
print(url) 