import requests

# API URL for creating a new order
url = "https://jsonplaceholder.typicode.com/posts"

# Order details
order_data = {
    "order_id": 102,
    "product": "Laptop1",
    "quantity": 2,
    "price": 1501
}

# Send POST request
postresponse = requests.post(url, json=order_data)

# Print the response
print("\n=== ORDER CREATED ===")
print("Status Code:", postresponse.status_code)  # Expected: 201 (Created)
print("Response:", postresponse.json())  # Order details

# Get the created order ID
order_id = postresponse.json().get("id")
print(order_id)
