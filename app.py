from flask import Flask, request
from playsound import playsound
import threading
import time

app = Flask(__name__)

alarm_seconds = 0
alarm_thread = None


def trigger_alarm():
    global alarm_seconds
    playsound("alarm.wav")
    alarm_seconds = 0


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/set_alarm')
def set_alarm():
    global alarm_seconds
    minutes = int(request.args.get('minutes', 0))
    seconds = int(request.args.get('seconds', 0))
    alarm_seconds = minutes * 60 + seconds
    return 'OK', 200


@app.route('/start_alarm')
def start_alarm():
    global alarm_thread
    if alarm_seconds > 0 and (alarm_thread is None or not alarm_thread.is_alive()):
        alarm_thread = threading.Thread(target=trigger_alarm)
        alarm_thread.start()
    return 'OK', 200


if __name__ == '__main__':
    app.run(debug=True)
