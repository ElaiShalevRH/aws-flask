from flask import Flask
from flask import request

app = Flask(__name__)

users = []
users.append({
    "name": "Marcin",
    "country": "Polska",
    "cat_amount": 3,
  })

@app.route("/users", methods=['GET'])
def get_user():
  if request.args.get('latest') == 'true': # return latest user
    return users[-1]
  return users # return all users


@app.route("/users", methods=['POST'])
def add_user():
  users.append(request.json)
  return {"response": "New User added successfully."}


