from flask import Flask, render_template
from datetime import datetime


app = Flask(__name__)
time = datetime.now()


@app.route('/')
def index():
    global time
    return render_template('index.html', time=datetime.timestamp(time))


@app.route('/api/get-time', methods=['GET'])
def get_time():
    global time
    return time.strftime('%s')


@app.route('/api/reset-time', methods=['GET'])
def reset_time():
    global time
    time = datetime.now()
    return ''
