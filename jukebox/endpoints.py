from flask import Flask
from flask import jsonify
from flask_cors import CORS
from flask import request
import psycopg2, json

app = Flask(__name__)
CORS(app)

# Connect to your postgres DB
conn = psycopg2.connect("dbname=makesong user=postgres")

# Open a cursor to perform database operations
cur = conn.cursor()


@app.route("/", methods=['POST', 'GET'])
def hello():
    return "hello"

@app.route("/save_email", methods=['POST'])
def save_email():

  email = request.form['email']
  print("trying to save", email)
  
  try: 
    cur.execute("INSERT INTO waitlist (email, created_at) VALUES ('{0}', now());".format(email))
    conn.commit()
    return jsonify({"success": True})
  except Exception as e: 
    return { "results": f"failed with error: {e}" }


