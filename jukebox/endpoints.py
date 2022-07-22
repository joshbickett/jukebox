from flask import Flask
from flask import jsonify
from flask_cors import CORS
from flask import request
import psycopg2, json
from sample import run

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

@app.route("/make", methods=['POST', 'GET'])
def make():
  try: 
    print("making song: ", request.form)
    lyrics = request.form['lyrics']
    lyrics = lyrics.replace("\r", ",")
    lyrics = lyrics.replace("\n", " ")
    print("lyrics,", lyrics)
    info = { "artist": "The Beatles", "genre": "Rock", "lyrics": lyrics}
    run(model='1b_lyrics', name='sample_1b', levels=3, sample_length_in_seconds=20, total_sample_length_in_seconds=180, sr=44100, n_samples=3, hop_fraction=(0.5,0.5,0.125), song_info=info)
    return jsonify({"success": True})
  except Exception as e:
    return { "results": f"failed with error: {e}" }
  

