import requests

response = requests.get("https://reqres.in/api/users")

data = response.json()['data']

for email in data:
    print(email["email"])

