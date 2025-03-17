import requests

url = "https://api.restful-api.dev/objects/7"
response = requests.get(url)

# Ensure the response is in JSON format
json_response = response.json()

# Check the type of the response to handle it properly
if isinstance(json_response, dict):    
    # If it's a dictionary, access using keys
    print(f"ID: {json_response['id']}")
