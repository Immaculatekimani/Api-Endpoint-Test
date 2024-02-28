import requests

# Base URL of the booking system API
BASE_URL = 'https://restful-booker.herokuapp.com/booking/'

# Function to send a PUT request to update a booking
def update_booking(booking_id, data):
    url = BASE_URL + str(booking_id)
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM='
    }
    response = requests.put(url, json=data, headers=headers)
    return response

# Positive Test Scenario: Update a booking with valid data and authentication
def test_positive_scenario():
    booking_id = 2
    data = {
        "firstname": "UpdatedFirstName",
        "lastname": "UpdatedLastName",
        "totalprice": 222,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-03-01",
            "checkout": "2024-03-05"
        },
        "additionalneeds": "Dinner"
    }
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM='
}
    response = update_booking(booking_id, data)
    print("Positive Test Scenario Response:")
    print("Status Code:", response.status_code)
    print("Response Body:", response.json())
    print()

# Negative Test Scenario: Attempt to update a booking with an invalid booking ID
def test_invalid_booking_id_scenario():
    invalid_booking_id = 9999
    data = {
        "firstname": "UpdatedFirstName",
        "lastname": "UpdatedLastName",
        "totalprice": 222,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-03-01",
            "checkout": "2024-03-05"
        },
        "additionalneeds": "Dinner"
    }
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM='
    }
    response = update_booking(invalid_booking_id, data)
    print("Negative Test Scenario: Invalid Booking ID Response:")
    print("Status Code:", response.status_code)
    print("Response Body:", response.text)
    print()

# Negative Test Scenario: Attempt to update a booking with missing required fields
def test_missing_fields_scenario():
    booking_id = 2
    data = {
        # Missing required fields
    }

    response = update_booking(booking_id, data)
    print("Negative Test Scenario: Missing Fields Response:")
    print("Status Code:", response.status_code)
    print("Response Body:", response.text)
    print()

# Negative Test Scenario: Attempt to update a booking with invalid data types
def test_invalid_data_types_scenario():
    booking_id = 2
    data = {
        "firstname": 123,  # Invalid data type
        "lastname": "UpdatedLastName",
        "totalprice": "222",  # Invalid data type
        "depositpaid": "True",  # Invalid data type
        "bookingdates": {
            "checkin": "2024-03-01",
            "checkout": "2024-03-05"
        },
        "additionalneeds": ["Dinner"]  # Invalid data type
    }
   
    response = update_booking(booking_id, data)
    print("Negative Test Scenario: Invalid Data Types Response:")
    print("Status Code:", response.status_code)
    print("Response Body:", response.text)
    print()

# Run test scenarios
if __name__ == "__main__":
    test_positive_scenario()
    test_invalid_booking_id_scenario()
    test_missing_fields_scenario()
    test_invalid_data_types_scenario()


