import requests

url = "https://api.themoviedb.org/3/authentication"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjMWM0OTFkNWVmYTQ2NGYyY2UwN2FjZDFhNDVlMGNjZSIsIm5iZiI6MTY0NjU4MjQ0OS43OTUsInN1YiI6IjYyMjRkYWIxZTMyM2YzMDA2Y2M2MzUyMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.v0ey8wMc2MTBA3wKf9PAqOob-w869JJoDegWDmru5-0"
}

response = requests.get(url, headers=headers)

print(response.text)