#this will automate the token handling

import requests
import configparser

#Load configuration from the config.ini file
config = configparser.ConfigParser()
config.read('config.ini')

#Function to log in and retrieve the token
def login_and_get_token():
    login_data = {
        "email": config['login']['email'],
        "password": config['login']['password']
    }

    #Send login request
    response = requests.post("https://reqres.in/api/login", json=login_data)

    if response.status_code == 200:
        return response.json().get("token")
    else:
        print("Login failed:", response.json())
        return None

#Function to fetch users using the token
def get_users(token):
    headers = {
        "Authorization": token
    }

    #Call the second API
    response = requests.get("https://reqres.in/api/users?page=2", headers=headers)

    if response.status_code == 200:
        print("Users fetched successfully:", response.json())
    else:
        print("Failed to fetch users:", response.json())

if __name__ == '__main__':
    token = login_and_get_token()
    if token:
        get_users(token)
