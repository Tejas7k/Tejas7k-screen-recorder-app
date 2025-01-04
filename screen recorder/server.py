from flask import Flask, jsonify
import threading
import subprocess

app = Flask(__name__)

recording_process = None

def start_recording():
    global recording_process
    recording_process = subprocess.Popen(["python", "screen_recorder.py"])

@app.route('/start-recording', methods=['POST'])
def start_recording_endpoint():
    threading.Thread(target=start_recording).start()
    return jsonify({"message": "Recording started!"})

@app.route('/stop-recording', methods=['POST'])
def stop_recording_endpoint():
    global recording_process
    if recording_process:
        recording_process.terminate()
        recording_process = None
    return jsonify({"message": "Recording stopped and saved!"})

if __name__ == "__main__":
    app.run(debug=True)
