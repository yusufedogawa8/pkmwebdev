from flask import Flask, render_template, jsonify
import subprocess

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/catspeaking.html')
def category():
    return render_template('catspeaking.html')

@app.route('/activity.html', methods=['GET'])
def speaking():
    # Render the activity.html page
    return render_template('activity.html')

@app.route('/get_speech_result', methods=['GET'])
def get_speech_result():
    try:
        with open("error.txt", "r") as error_file:
            error_message = error_file.read()
    except FileNotFoundError:
        error_message = "Pesan kesalahan tidak ditemukan."

    return jsonify({'result': error_message})

@app.route('/run_main', methods=['POST'])
def run_main():
    result = subprocess.run(["python", "main.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout

if __name__ == '__main__':
    app.run(debug=True)
