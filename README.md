# Flask API Automation with Token Handling

## Overview

This Flask application automates the process of logging into an API, retrieving a token, and using that token to access a second API. The app demonstrates how to manage authentication via tokens and how to pass the token between requests automatically.

### Features:
1. **Login API**: POST request to authenticate a user and get an authorization token.
2. **User Data API**: GET request to fetch user data using the authorization token.

---

## Setup Instructions

### 1. Prerequisites
- Python 3.x
- Flask
- `requests` library
- `configparser` library

### 2. Install Dependencies

Run the following command to install the necessary dependencies:

```bash
pip install flask requests configparser

#++++++++++++++++++++++++++++++++++ Testing the application ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
You can test the Flask application using Postman or cURL to verify the functionality of the API endpoints.

1. Testing the Login API
Endpoint: /login
Method: POST
URL: http://127.0.0.1:5000/login

Request:
Headers:
Content-Type: application/json
Body:
json
Copy code
{
  "email": "eve.holt@reqres.in",
  "password": "cityslicka"
}
(Use the credentials from your config.ini file.)

Expected Response:
On success:

json
Copy code
{
  "message": "Login successful",
  "token": "your_generated_token"
}
On failure (e.g., invalid credentials):

json
Copy code
{
  "message": "Login failed",
  "error": "Invalid credentials or error details"
}
Testing with cURL:
bash
Copy code
curl -X POST http://127.0.0.1:5000/login -H "Content-Type: application/json" -d "{\"email\": \"eve.holt@reqres.in\", \"password\": \"cityslicka\"}"
Testing with Postman:
Open Postman and create a new POST request.
Set the URL to http://127.0.0.1:5000/login.
Set the Headers:
Key: Content-Type, Value: application/json.
In the Body, choose raw and paste the JSON:
json
Copy code
{
  "email": "eve.holt@reqres.in",
  "password": "cityslicka"
}
Send the request. You should receive a token in the response.


2. Testing the Users API
Endpoint: /users
Method: GET
URL: http://127.0.0.1:5000/users

Request:
Headers:
Authorization: Bearer <your_generated_token>
The token must be obtained from the /login endpoint.

Expected Response:
On success:

json
Copy code
{
  "page": 2,
  "per_page": 6,
  "total": 12,
  "total_pages": 2,
  "data": [
    {
      "id": 7,
      "email": "michael.lawson@reqres.in",
      "first_name": "Michael",
      "last_name": "Lawson",
      "avatar": "https://reqres.in/img/faces/7-image.jpg"
    },
    {
      "id": 8,
      "email": "lindsay.ferguson@reqres.in",
      "first_name": "Lindsay",
      "last_name": "Ferguson",
      "avatar": "https://reqres.in/img/faces/8-image.jpg"
    },
    ...
  ]
}
Testing with cURL:
bash
Copy code
curl -X GET http://127.0.0.1:5000/users -H "Authorization: Bearer <your_token_here>"
Testing with Postman:
Create a new GET request in Postman.
Set the URL to http://127.0.0.1:5000/users.
In the Authorization tab, choose Bearer Token and paste the token you received from the /login response.
Send the request to fetch the users.
