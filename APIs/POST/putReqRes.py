import requests

# API URL for the PUT request
url = "https://jsonplaceholder.typicode.com/posts/1"

# Data to be sent in the PUT request
data = {
    "id": 1,
    "title": "Updated Title",
    "body": "This is the updated body of the post.",
    "userId": 1
}

# Sending the PUT request
response = requests.put(url, json=data)

# Printing the response
print("Status Code:", response.status_code)
print("Response JSON:", response.json())
