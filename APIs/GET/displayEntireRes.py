import requests

url = "https://api.restful-api.dev/objects/7"
response = requests.get(url)

# Parse the response as JSON
json_response = response.json()

# Check if the response is a list
if isinstance(json_response, list):
    # Loop through all items in the list and print each item
    for item in json_response:
        print(item)  # Add a newline after each item
else:
    # If it's not a list, print the item directly as a dictionary
    print(json_response)
