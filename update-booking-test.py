import requests
import base64

url = 'https://restful-booker.herokuapp.com/booking/2'
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM='
}
data = {
    "firstname": "James",
    "lastname": "Brown",
    "totalprice": 111,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2024-02-25",
        "checkout": "2024-02-27"
    },
    "additionalneeds": "Breakfast"
}

response = requests.put(url, json=data, headers=headers)

print(response.status_code)
print(response.json())
