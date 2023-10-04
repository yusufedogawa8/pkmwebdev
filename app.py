from flask import Flask, render_template, redirect, url_for
import subprocess

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/catspeaking.html')
def category():
    return render_template('catspeaking.html')

@app.route('/speaking.html', methods=['GET'])
def speaking():
    # Render the speaking.html page
    return render_template('speaking.html')

@app.route('/run_main', methods=['POST'])
def run_main():
    result = subprocess.run(["python", "main.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout

if __name__ == '__main__':
    app.run(debug=True)
