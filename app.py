from flask import Flask, jsonify, request
import requests
import configparser

app = Flask(__name__)

#Load configuration from the config.ini file
config = configparser.ConfigParser()
config.read('config.ini')

#This is a default page for the flask application
@app.route('/', methods=['GET'])
def index():
    return jsonify({"message": "Welcome to the API. Use /login to log in."}), 200


#Route for login 
@app.route('/login', methods=['POST'])
def login():
    login_data = {
        "email": config['login']['email'],
        "password": config['login']['password']
    }

    #Send login request
    response = requests.post("https://reqres.in/api/login", json=login_data)

    if response.status_code == 200:
        token = response.json().get("token")
        #Return token to the client
        return jsonify({"message": "Login successful", "token": token}), 200
    else:
        return jsonify({"message": "Login failed", "error": response.json()}), response.status_code

#Route to access the second API
@app.route('/users', methods=['GET'])
def get_users():
    token = request.headers.get("Authorization")  #Get token from headers
    if not token:
        return jsonify({"message": "Token is missing"}), 401
    
    headers = {
        "Authorization": token  #use the token in the Authorization header
    }
    
    #call the second API
    response = requests.get("https://reqres.in/api/users?page=2", headers=headers)
    
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({"message": "Failed to fetch users", "error": response.json()}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
