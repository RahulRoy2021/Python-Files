from flask import Flask, request, render_template, redirect
from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb://localhost:27017")
db = client["naya"]
collection = db["btech"]

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    username = request.form["username"]
    password = request.form["password"]
    collection.insert_one({"username": username, "password": password})
    data = collection.find()
    return render_template("dashboard.html", data=data)

@app.route('/update', methods=["GET","POST"])
def update():
    # Retrieve the form data
    user_id = request.form.get("user_id")
    new_username = request.form.get("new_username")
    print("User ID:", user_id)  # Debugging print statement
    print("New Username:", new_username)  # Debugging print statement

    # Check if both user_id and new_username are present
    if user_id and new_username:
        # Update the username in the database
        collection.update_one({"_id": ObjectId(user_id)}, {"$set": {"username": new_username}})
        # Redirect to the index page to fetch and display the updated data
        return redirect('/')
    else:
        return "Error: User ID or new username missing."
if __name__ == '__main__':
    app.run(debug=True)
