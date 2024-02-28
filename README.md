## Update Booking Endpoint Testing

This script demonstrates how to update a booking using the RESTful Booker API with Python.

### Overview

The script sends a PUT request to update a booking with the provided data. It includes Basic authentication credentials in the request headers.

### Requirements

- Python 3.x
- `requests` library

### Usage

1. Copy the script into a Python file (e.g., `test-scenarios.py`).
2. Update the script with the appropriate Base URL, booking ID, data, and headers.
3. Run the script using the following command:
    ```
    python test-scenarios.py
    ```

### Script Explanation

- **Base URL**: The base URL of the booking system API.
- **Function `update_booking()`**: Sends a PUT request to update a booking.
- **Positive Test Scenario**: Updates a booking with valid data and authentication.
- **Negative Test Scenario**: Attempts to update a booking with an invalid booking ID.
- **Additional Scenarios**: Test scenarios for missing fields and invalid data types.

### Test Scenarios

#### Positive Test Scenario

- Updates a booking with valid data and authentication.
- Verifies the response status code and JSON response.
- If the status code is 200, the booking was successfully updated.
- If the status code is 403, there may be an issue with authentication or insufficient permissions.

#### Negative Test Scenario

- Attempts to update a booking with an invalid booking ID.
- Verifies the response status code and error message.
- If the status code is 405, then this affirms that the ID is invalid.

#### Additional Scenarios

- **Missing Fields Scenario**: Attempts to update a booking with missing required fields.
    - Verifies the response status code and error message.
    - If the status code is 400, then this indicates a bad request due to missing fields.

- **Invalid Data Types Scenario**: Attempts to update a booking with invalid data types.
    - Verifies the response status code and error message.
    - If the status code is 500, then this indicates an internal server error caused by invalid data types.

### Implementation Details

- The script uses Basic authentication with a hardcoded username and password encoded in Base64.

### Contributors

- Immaculate Kimani

### License

This project is licensed under the [MIT License](LICENSE).
