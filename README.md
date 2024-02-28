# Update Booking Endpoint Testing

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Install Python from [python.org](https://www.python.org/downloads/)
2. Install the `requests` library by running:
    ```
    pip install requests
    ```

## Usage

1. Clone this repository or copy the provided Python script into your project directory.
2. Update the script with the appropriate URL, authentication token, and booking details.
3. Run the script using the following command:
    ```
    python update_booking.py
    ```

## Authentication

The script supports two methods of authentication:

- Cookie: Provide the authentication token in the `Cookie` header.
- Basic: Provide the username and password encoded in Base64 in the `Authorization` header.

Choose one method based on the API's authentication requirements.

## Response

The script prints the status code and JSON response received from the server.

- If the status code is `200`, the booking was successfully updated.
- If the status code is `403`, there may be an issue with authentication or insufficient permissions.

## Troubleshooting

If you encounter any issues, consider the following:

- Double-check the URL of the API endpoint.
- Ensure that the authentication token or Basic authentication credentials are correct.
- Review the API documentation for any specific requirements or limitations.

## Contributors

- Immaculate Kimani

## License

This project is licensed under the [MIT License](LICENSE).
