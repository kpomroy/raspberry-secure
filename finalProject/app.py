from flask import *
import mysql.connector
import json
import os

app = Flask(__name__)

credentials = json.load(open("credentials.json", "r"))

@app.route('/videos', methods=['GET'])
def temp():
    database = mysql.connector.connect(
        host=credentials["host"],
        user=credentials["user"],
        passwd=credentials["password"],
        database=credentials["database"]
    )
    cursor = database.cursor()

    # Query to get records
    query = "SELECT * FROM videos;"
    cursor.execute(query)
    data = cursor.fetchall()

    cursor.close()
    database.close()
    return render_template("video_chart.html", data = data, name = 'Raspberry Secure')

@app.route('/control', methods=['GET'])
def cont():
    return render_template("control.html")

@app.route('/activate', methods=['POST'])
def act():
    os.system('python3 /home/kpomroy/Desktop/CS121/finalProject/video.py')
    return "ok"

@app.route('/deactivate', methods=['POST'])
def deact():
    os.system('pkill -f video.py')
    return "ok"

@app.route('/', methods=['GET'])
def default():
    return redirect(url_for('videos'))


