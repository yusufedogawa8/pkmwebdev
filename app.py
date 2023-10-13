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
def activity():
    # Render the activity.html page
    return render_template('activity.html')

@app.route('/hobby.html', methods=['GET'])
def hobby():
    # Render the activity.html page
    return render_template('hobby.html')

@app.route('/introduction.html', methods=['GET'])
def introduction():
    # Render the activity.html page
    return render_template('introduction.html')

@app.route('/angka.html', methods=['GET'])
def angka():
    # Render the activity.html page
    return render_template('angka.html')

@app.route('/run_main', methods=['POST'])
def run_main():
    result = subprocess.run(["python", "main.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout

@app.route('/run_introduction', methods=['POST'])
def run_introduction():
    result = subprocess.run(["python", "introduction.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout

@app.route('/run_hobby', methods=['POST'])
def run_hobby():
    result = subprocess.run(["python", "hobby.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout

@app.route('/run_angka', methods=['POST'])
def run_angka():
    result = subprocess.run(["python", "angka.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout

if __name__ == '__main__':
    app.run(debug=True)
