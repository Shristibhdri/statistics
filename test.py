import requests

url = "http://127.0.0.1:8000"

request = requests.post(url + "/api/factorial", data = {
    "num": 10
})
print(request.json())

request = requests.post(url + "/api/median", data = {
    "num": "4,2,7,18,32,37,20,48,6,9"
})
print(request.json())

request = requests.post(url + "/api/variance", data = {
    "num": "6,28,91,6,4,2,10,498,77,20"
})
print(request.json())

request = requests.post(url +"/api/pstdev", data = {
    "num": "2,4,91,90,54,2,7,82,19,1"
})
print(request.json())