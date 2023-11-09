from flask import Flask, render_template
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

@app.route('/vocab.html', methods=['GET'])
def vocab():
    # Render the vocab.html page
    return render_template('vocab.html')

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

@app.route('/angka20.html', methods=['GET'])
def angka20():
    # Render the activity.html page
    return render_template('angka20.html')

@app.route('/tempat.html', methods=['GET'])
def tempat():
    # Render the activity.html page
    return render_template('tempat.html')

@app.route('/makanan.html', methods=['GET'])
def makanan():
    # Render the activity.html page
    return render_template('makanan.html')

@app.route('/restoran.html', methods=['GET'])
def restoran():
    # Render the activity.html page
    return render_template('restoran.html')

@app.route('/baju.html', methods=['GET'])
def baju():
    # Render the activity.html page
    return render_template('baju.html')

@app.route('/dokter.html', methods=['GET'])
def dokter():
    # Render the activity.html page
    return render_template('dokter.html')

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

@app.route('/run_angka20', methods=['POST'])
def run_angka20():
    result = subprocess.run(["python", "angka20.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout

@app.route('/run_tempat', methods=['POST'])
def run_tempat():
    result = subprocess.run(["python", "tempat.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout

@app.route('/run_makanan', methods=['POST'])
def run_makanan():
    result = subprocess.run(["python", "makanan.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout

@app.route('/run_restoran', methods=['POST'])
def run_restoran():
    result = subprocess.run(["python", "restoran.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout

@app.route('/run_baju', methods=['POST'])
def run_baju():
    result = subprocess.run(["python", "baju.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout

@app.route('/run_dokter', methods=['POST'])
def run_dokter():
    result = subprocess.run(["python", "dokter.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout

if __name__ == '__main__':
    app.run(debug=True)
