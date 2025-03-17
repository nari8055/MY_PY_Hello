import requests

# API URL for the DELETE request
url = "https://jsonplaceholder.typicode.com/posts/1"

# Sending the DELETE request
response = requests.delete(url)

# Printing the response
print("Status Code:", response.status_code)
print("Response Text:", response.text)  # Usually empty
