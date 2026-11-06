import requests

response = requests.get("https://jsonplaceholder.typicode.com/users/1")
print(response.status_code)
print(response.json)
print(response.elapsed.total_seconds())