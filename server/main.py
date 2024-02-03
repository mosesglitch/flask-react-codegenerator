from flask import Flask
from dotenv import load_dotenv
import request
import os

app=Flask(__name__)

load_dotenv()

db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")

@app.route("/myinput",["POST"])
def getinference():
    return "It"


@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    return f'Submitted data: {data}'

if __name__=='__main__':
    app.run(debug=True,port=5000)