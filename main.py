from flask import Flask, render_template

app = Flask(__name__, static_folder="Static", template_folder="templates")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/diakonia')
def diakonia():
    return render_template('diakonia.html')

@app.route('/koinonia')
def koinonia():
    return render_template('koinonia.html')

@app.route('/marturia')
def marturia():
    return render_template('marturia.html')

@app.route('/organisasi')
def organisasi():
    return render_template('organisasi.html')

@app.route('/warta')
def warta():
    return render_template('warta.html')

if __name__ == '__main__':
    app.run(debug=True)
