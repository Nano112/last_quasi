from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

time = datetime.now()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/get-time', methods=['GET'])
def get_time():
    print(time)
    return time.strftime('%s')

@app.route('/api/reset-time', methods=['GET'])
def reset_time():
    global time
    time = datetime.now()
    print(time)
    return ''
