from flask import Flask
from flask import request


app = Flask(__name__)

users = []
users.append({
    "name": "Marcin",
    "country": "Polska",
    "cat_amount": 3,
  })

@app.route("/user/latest", methods=['GET'])
def get_latest_user():
  return users[-1]

@app.route("/user/all", methods=['GET'])
def get_all_users():
  return users

@app.route("/user/upload", methods=['POST'])
def send_data():
  data = request.json
  users.append(data)
  return "Successs."

