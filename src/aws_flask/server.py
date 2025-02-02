from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/', endpoint='home')
def home():
    return render_template('index.html') 
@app.route('/info')
def info():
    return render_template('info.html')  


users = []
users.append({
    "name": "Marcin",
    "country": "Polska",
    "cat_amount": 3,
  })

@app.route("/api/users", methods=['GET'])
def get_user():
  if request.args.get('latest') == 'true': # return latest user
    return users[-1]
  return users # return all users


@app.route("/api/users", methods=['POST'])
def add_user():
  users.append(request.json)
  return {"response": "New User added successfully."}

