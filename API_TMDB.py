import requests

url = "https://api.themoviedb.org/3/authentication"

headers = {
    "accept": "application/json",
    "Authorization": <seu cabesalho>
}

response = requests.get(url, headers=headers)

print(response.text)